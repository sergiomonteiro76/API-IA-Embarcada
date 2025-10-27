[README.md](https://github.com/user-attachments/files/23174064/README.md)
# 🚀 API de IA Simples - Versão Leve e Fácil

## ✨ Versão Simplificada

Esta é uma versão **super simplificada** da API de IA que:

- ✅ **Modelos pequenos** (~100MB ao invés de 3GB)
- ✅ **Instalação rápida** (2-3 minutos)
- ✅ **Funciona em qualquer PC**
- ✅ **Fácil de desinstalar**
- ✅ **Sem complicações**

## 🎯 Funcionalidades

1. **Análise de Sentimento** - Detecta se um texto é positivo, negativo ou neutro
2. **Geração de Texto** - Cria textos em português
3. **Resumo de Texto** - Resume textos longos (método simplificado)

## ⚡ Instalação Rápida (3 Passos)

### Windows

```powershell
# 1. Criar ambiente virtual
python -m venv venv
.\venv\Scripts\Activate.ps1

# 2. Instalar (SEM requirements.txt)
pip install flask transformers torch

# 3. Executar
python app.py
```

### Linux/macOS

```bash
# 1. Criar ambiente virtual
python3 -m venv venv
source venv/bin/activate

# 2. Instalar
pip install flask transformers torch

# 3. Executar
python app.py
```

## 🌐 Usar

Acesse: **http://localhost:5000**

## 🗑️ Desinstalar

```powershell
# Desativar ambiente virtual
deactivate

# Deletar a pasta do projeto
# (isso remove TUDO, incluindo os modelos)
```

## 💡 Por Que Esta Versão?

| Aspecto | Versão Completa | Versão Simples |
|---------|----------------|----------------|
| **Tamanho dos modelos** | ~3GB | ~100MB |
| **Tempo de download** | 10-15 min | 2-3 min |
| **Requisitos** | 8GB RAM | 4GB RAM |
| **Dependências** | 6 pacotes | 3 pacotes |
| **Complexidade** | Média | Baixa |
| **Ideal para** | Produção | Aprendizado |

## 📦 Estrutura

```
api_ia_simples/
├── app.py                 # Aplicação Flask
├── servicos/
│   └── servico_ia.py     # Modelos leves
├── static/               # CSS e JS
├── templates/            # Interface HTML
└── requirements.txt      # Apenas 3 linhas!
```

## ✅ Testado e Funcionando

- ✅ Windows 10/11
- ✅ macOS
- ✅ Linux
- ✅ Python 3.9+

---

**Simples, rápido e funcional!** 🎉

