"""
Serviço de Inteligência Artificial - VERSÃO SIMPLIFICADA
Este módulo usa modelos pequenos e leves do Hugging Face.

VANTAGENS:
- Download rápido (~100MB ao invés de 3GB)
- Instalação simples
- Funciona em qualquer computador
- Fácil de desinstalar
"""
# Adicione esta linha no início do arquivo
import torch

# O restante do arquivo permanece o mesmo
from transformers import pipeline
import warnings

# Suprime avisos desnecessários
warnings.filterwarnings('ignore')

# ==================== CACHE DOS MODELOS ====================

_cache_modelos = {}

def obter_modelo_sentimento():
    """
    Obtém o pipeline de análise de sentimento.
    Usa um modelo MUITO LEVE e rápido.
    """
    if 'sentimento' not in _cache_modelos:
        print("📥 Carregando modelo de sentimento (pequeno e rápido)...")
        # Modelo leve de análise de sentimento em português
        # Tamanho: ~50MB
        _cache_modelos['sentimento'] = pipeline(
            "sentiment-analysis",
            model="lxyuan/distilbert-base-multilingual-cased-sentiments-student",
            device=-1  # Sempre usa CPU (mais compatível)
        )
        print("✅ Modelo de sentimento carregado!")
    return _cache_modelos['sentimento']

def obter_modelo_geracao():
    """
    Obtém o modelo de geração de texto.
    Usa um modelo pequeno e eficiente.
    """
    if 'geracao' not in _cache_modelos:
        print("📥 Carregando modelo de geração (pequeno e rápido)...")
        # Modelo GPT-2 pequeno em português
        # Tamanho: ~50MB
        _cache_modelos['geracao'] = pipeline(
            "text-generation",
            model="pierreguillou/gpt2-small-portuguese",
            device=-1  # Sempre usa CPU
        )
        print("✅ Modelo de geração carregado!")
    return _cache_modelos['geracao']

# ==================== FUNÇÕES DE IA ====================

def analisar_sentimento(texto):
    """
    Analisa o sentimento de um texto usando IA local.
    
    Parâmetros:
        texto (str): O texto a ser analisado
        
    Retorna:
        dict: Dicionário contendo o sentimento e a confiança da análise
    """
    try:
        # Obtém o modelo
        classificador = obter_modelo_sentimento()
        
        # Faz a análise
        resultado = classificador(texto)[0]
        
        # Converte o resultado para formato padronizado
        label = resultado['label'].upper()
        confianca = resultado['score']
        
        # Mapeia os labels para português
        mapa_sentimentos = {
            'POSITIVE': 'POSITIVO',
            'NEGATIVE': 'NEGATIVO',
            'NEUTRAL': 'NEUTRO'
        }
        
        sentimento = mapa_sentimentos.get(label, label)
        
        return {
            "sucesso": True,
            "sentimento": sentimento,
            "confianca": round(confianca * 100, 2),
            "texto_original": texto,
            "detalhes": f"{sentimento} ({confianca:.2%})"
        }
        
    except Exception as erro:
        return {
            "sucesso": False,
            "erro": str(erro),
            "mensagem": "Erro ao analisar sentimento"
        }


def gerar_texto(tema, tamanho="medio"):
    """
    Gera um texto criativo sobre um tema específico usando IA local.
    
    Parâmetros:
        tema (str): O tema sobre o qual gerar o texto
        tamanho (str): Tamanho do texto (curto, medio, longo)
        
    Retorna:
        dict: Dicionário contendo o texto gerado
    """
    try:
        # Obtém o modelo
        gerador = obter_modelo_geracao()
        
        # Define o número de tokens baseado no tamanho
        tokens_por_tamanho = {
            "curto": 50,
            "medio": 100,
            "longo": 150
        }
        
        max_tokens = tokens_por_tamanho.get(tamanho, 100)
        
        # Cria o prompt inicial
        prompt = f"{tema}."
        
        # Gera o texto
        resultado = gerador(
            prompt,
            max_new_tokens=max_tokens,
            num_return_sequences=1,
            temperature=0.7,
            top_k=50,
            top_p=0.9,
            do_sample=True,
            repetition_penalty=1.2,
            pad_token_id=50256
        )
        
        # Extrai o texto gerado
        texto_gerado = resultado[0]['generated_text']
        
        # Remove o prompt inicial se estiver presente
        if texto_gerado.startswith(prompt):
            texto_gerado = texto_gerado[len(prompt):].strip()
        
        return {
            "sucesso": True,
            "tema": tema,
            "texto_gerado": texto_gerado,
            "tamanho_solicitado": tamanho,
            "palavras_geradas": len(texto_gerado.split())
        }
        
    except Exception as erro:
        return {
            "sucesso": False,
            "erro": str(erro),
            "mensagem": "Erro ao gerar texto"
        }


def resumir_texto(texto, tamanho_resumo="medio"):
    """
    Resume um texto de forma simples (extração de frases principais).
    Versão simplificada que não requer modelos pesados.
    
    Parâmetros:
        texto (str): O texto a ser resumido
        tamanho_resumo (str): Tamanho do resumo (curto, medio, longo)
        
    Retorna:
        dict: Dicionário contendo o resumo do texto
    """
    try:
        # Resumo simples: pega as primeiras frases
        frases = texto.split('.')
        frases = [f.strip() for f in frases if f.strip()]
        
        # Define quantas frases incluir baseado no tamanho
        num_frases = {
            "curto": 1,
            "medio": 2,
            "longo": 3
        }
        
        n = num_frases.get(tamanho_resumo, 2)
        resumo = '. '.join(frases[:n]) + '.'
        
        return {
            "sucesso": True,
            "texto_original": texto,
            "resumo": resumo,
            "tamanho_resumo": tamanho_resumo,
            "reducao": f"{len(resumo)}/{len(texto)} caracteres",
            "nota": "Resumo por extração de frases (método simplificado)"
        }
        
    except Exception as erro:
        return {
            "sucesso": False,
            "erro": str(erro),
            "mensagem": "Erro ao resumir texto"
        }


def obter_informacoes_modelo():
    """
    Retorna informações sobre os modelos de IA sendo utilizados.
    
    Retorna:
        dict: Informações sobre os modelos
    """
    return {
        "modelos": {
            "sentimento": "lxyuan/distilbert-base-multilingual-cased-sentiments-student",
            "geracao": "pierreguillou/gpt2-small-portuguese",
            "resumo": "Método simplificado (extração de frases)"
        },
        "provedor": "Hugging Face (Modelos Leves)",
        "descricao": "Modelos pequenos e rápidos, ideais para aprendizado",
        "dispositivo": "CPU",
        "tamanho_total": "~100MB (muito menor que versões completas)",
        "capacidades": [
            "Análise de sentimentos (rápida)",
            "Geração de texto em português",
            "Resumo simples de texto",
            "Execução 100% local"
        ],
        "vantagens": [
            "Download rápido (~2 minutos)",
            "Funciona em qualquer computador",
            "Sem custos de API",
            "Fácil de desinstalar",
            "Privacidade total"
        ]
    }


def pre_carregar_modelos():
    """
    Pré-carrega os modelos na inicialização da aplicação.
    """
    print("\n" + "="*60)
    print("🤖 Pré-carregando modelos de IA (versão leve)...")
    print("="*60)
    
    try:
        print("\n1/2 Carregando modelo de sentimento...")
        obter_modelo_sentimento()
        
        print("\n2/2 Carregando modelo de geração...")
        obter_modelo_geracao()
        
        print("\n" + "="*60)
        print("✅ Todos os modelos foram carregados!")
        print("💡 Tamanho total: ~100MB (muito leve!)")
        print("="*60 + "\n")
        
    except Exception as erro:
        print(f"\n⚠️  Aviso: Erro ao pré-carregar modelos: {erro}")
        print("Os modelos serão carregados sob demanda.\n")

