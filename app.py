"""
API de Inteligência Artificial - Aplicação Principal
Este arquivo contém a aplicação Flask com todos os endpoints da API.
"""

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from servicos.servico_ia import (
    analisar_sentimento, 
    gerar_texto, 
    resumir_texto,
    obter_informacoes_modelo,
    pre_carregar_modelos
)
import os

# Inicializa a aplicação Flask
app = Flask(__name__)

# Configuração CORS - permite requisições do frontend
CORS(app)

# Configurações da aplicação
app.config['JSON_AS_ASCII'] = False  # Permite caracteres UTF-8 no JSON
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True  # JSON formatado


# ==================== ROTAS DA INTERFACE WEB ====================

@app.route('/')
def pagina_inicial():
    """
    Renderiza a página inicial com a interface web.
    """
    return render_template('index.html')


# ==================== ENDPOINTS DA API ====================

@app.route('/api/status', methods=['GET'])
def verificar_status():
    """
    Endpoint para verificar se a API está funcionando.
    
    Retorna:
        JSON com o status da API
    """
    return jsonify({
        "status": "online",
        "mensagem": "API de IA está funcionando corretamente!",
        "versao": "1.0.0",
        "endpoints_disponiveis": [
            "/api/status",
            "/api/modelo",
            "/api/sentimento",
            "/api/gerar",
            "/api/resumir"
        ]
    })


@app.route('/api/modelo', methods=['GET'])
def informacoes_modelo():
    """
    Endpoint que retorna informações sobre o modelo de IA.
    
    Retorna:
        JSON com informações do modelo
    """
    info = obter_informacoes_modelo()
    return jsonify(info)


@app.route('/api/sentimento', methods=['POST'])
def analisar_sentimento_endpoint():
    """
    Endpoint para análise de sentimento de um texto.
    
    Corpo da requisição (JSON):
        {
            "texto": "Texto a ser analisado"
        }
    
    Retorna:
        JSON com o resultado da análise
    """
    try:
        # Obtém os dados da requisição
        dados = request.get_json()
        
        # Valida se o texto foi fornecido
        if not dados or 'texto' not in dados:
            return jsonify({
                "sucesso": False,
                "erro": "Campo 'texto' é obrigatório"
            }), 400
        
        texto = dados['texto']
        
        # Valida se o texto não está vazio
        if not texto.strip():
            return jsonify({
                "sucesso": False,
                "erro": "O texto não pode estar vazio"
            }), 400
        
        # Chama o serviço de análise de sentimento
        resultado = analisar_sentimento(texto)
        
        # Retorna o resultado
        if resultado['sucesso']:
            return jsonify(resultado), 200
        else:
            return jsonify(resultado), 500
            
    except Exception as erro:
        return jsonify({
            "sucesso": False,
            "erro": str(erro),
            "mensagem": "Erro ao processar requisição"
        }), 500


@app.route('/api/gerar', methods=['POST'])
def gerar_texto_endpoint():
    """
    Endpoint para geração de texto sobre um tema.
    
    Corpo da requisição (JSON):
        {
            "tema": "Tema do texto",
            "tamanho": "curto|medio|longo" (opcional, padrão: medio)
        }
    
    Retorna:
        JSON com o texto gerado
    """
    try:
        # Obtém os dados da requisição
        dados = request.get_json()
        
        # Valida se o tema foi fornecido
        if not dados or 'tema' not in dados:
            return jsonify({
                "sucesso": False,
                "erro": "Campo 'tema' é obrigatório"
            }), 400
        
        tema = dados['tema']
        tamanho = dados.get('tamanho', 'medio')
        
        # Valida o tamanho
        if tamanho not in ['curto', 'medio', 'longo']:
            return jsonify({
                "sucesso": False,
                "erro": "Tamanho deve ser: curto, medio ou longo"
            }), 400
        
        # Valida se o tema não está vazio
        if not tema.strip():
            return jsonify({
                "sucesso": False,
                "erro": "O tema não pode estar vazio"
            }), 400
        
        # Chama o serviço de geração de texto
        resultado = gerar_texto(tema, tamanho)
        
        # Retorna o resultado
        if resultado['sucesso']:
            return jsonify(resultado), 200
        else:
            return jsonify(resultado), 500
            
    except Exception as erro:
        return jsonify({
            "sucesso": False,
            "erro": str(erro),
            "mensagem": "Erro ao processar requisição"
        }), 500


@app.route('/api/resumir', methods=['POST'])
def resumir_texto_endpoint():
    """
    Endpoint para resumir um texto.
    
    Corpo da requisição (JSON):
        {
            "texto": "Texto a ser resumido",
            "tamanho_resumo": "curto|medio|longo" (opcional, padrão: medio)
        }
    
    Retorna:
        JSON com o resumo do texto
    """
    try:
        # Obtém os dados da requisição
        dados = request.get_json()
        
        # Valida se o texto foi fornecido
        if not dados or 'texto' not in dados:
            return jsonify({
                "sucesso": False,
                "erro": "Campo 'texto' é obrigatório"
            }), 400
        
        texto = dados['texto']
        tamanho_resumo = dados.get('tamanho_resumo', 'medio')
        
        # Valida o tamanho do resumo
        if tamanho_resumo not in ['curto', 'medio', 'longo']:
            return jsonify({
                "sucesso": False,
                "erro": "Tamanho do resumo deve ser: curto, medio ou longo"
            }), 400
        
        # Valida se o texto não está vazio
        if not texto.strip():
            return jsonify({
                "sucesso": False,
                "erro": "O texto não pode estar vazio"
            }), 400
        
        # Chama o serviço de resumo
        resultado = resumir_texto(texto, tamanho_resumo)
        
        # Retorna o resultado
        if resultado['sucesso']:
            return jsonify(resultado), 200
        else:
            return jsonify(resultado), 500
            
    except Exception as erro:
        return jsonify({
            "sucesso": False,
            "erro": str(erro),
            "mensagem": "Erro ao processar requisição"
        }), 500


# ==================== TRATAMENTO DE ERROS ====================

@app.errorhandler(404)
def nao_encontrado(erro):
    """
    Tratamento para rotas não encontradas.
    """
    return jsonify({
        "sucesso": False,
        "erro": "Endpoint não encontrado",
        "mensagem": "Verifique a documentação da API"
    }), 404


@app.errorhandler(405)
def metodo_nao_permitido(erro):
    """
    Tratamento para métodos HTTP não permitidos.
    """
    return jsonify({
        "sucesso": False,
        "erro": "Método HTTP não permitido",
        "mensagem": "Verifique o método HTTP correto para este endpoint"
    }), 405


@app.errorhandler(500)
def erro_interno(erro):
    """
    Tratamento para erros internos do servidor.
    """
    return jsonify({
        "sucesso": False,
        "erro": "Erro interno do servidor",
        "mensagem": "Ocorreu um erro inesperado"
    }), 500


# ==================== INICIALIZAÇÃO ====================

if __name__ == '__main__':
    print("\n" + "="*60)
    print("🚀 API de Inteligência Artificial")
    print("="*60)
    print("📍 Interface Web: http://localhost:5000")
    print("📍 API Base URL: http://localhost:5000/api")
    print("💡 Usando modelos locais do Hugging Face (sem API keys!)")
    print("="*60)
    
    # Pré-carrega os modelos de IA
    pre_carregar_modelos()
    
    print("\n" + "="*60)
    print("🌐 Iniciando servidor Flask...")
    print("="*60 + "\n")
    
    # Inicia o servidor Flask
    app.run(
        host='0.0.0.0',  # Aceita conexões de qualquer IP
        port=5000,        # Porta padrão
        debug=False       # Debug desligado para evitar reload duplo
    )
