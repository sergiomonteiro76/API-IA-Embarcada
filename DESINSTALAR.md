# 🗑️ Como Desinstalar Completamente

## 🎯 Desinstalação Rápida

### Passo 1: Desativar Ambiente Virtual

Se o ambiente virtual estiver ativo `(venv)`, desative:

```powershell
deactivate
```

### Passo 2: Fechar o Terminal/PowerShell

Feche completamente o PowerShell ou terminal.

### Passo 3: Deletar a Pasta do Projeto

Simplesmente **delete a pasta** `api_ia_simples` (ou o nome que você deu).

Isso remove:
- ✅ A aplicação
- ✅ O ambiente virtual
- ✅ Todas as dependências instaladas no venv

---

## 🧹 Limpeza Completa (Liberar Espaço)

Os modelos de IA ficam em **cache** separado. Para remover completamente:

### Windows

1. Abra o Explorador de Arquivos
2. Cole este caminho na barra de endereços:
   ```
   %USERPROFILE%\.cache\huggingface
   ```
3. Delete a pasta `huggingface`

**OU** via PowerShell:
```powershell
Remove-Item -Recurse -Force "$env:USERPROFILE\.cache\huggingface"
```

### Linux/macOS

```bash
rm -rf ~/.cache/huggingface
```

---

## 📊 Quanto Espaço Vou Liberar?

| Item | Tamanho Aproximado |
|------|-------------------|
| Pasta do projeto (com venv) | ~200MB |
| Cache dos modelos | ~100MB |
| **Total** | **~300MB** |

---

## 🔄 Reinstalar Depois

Se quiser reinstalar no futuro, é só:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install flask transformers torch
python app.py
```

Os modelos serão baixados novamente (rápido, ~2 minutos).

---

## ✅ Verificar se Foi Removido

Para ter certeza que tudo foi removido:

```powershell
# Verificar se a pasta existe
Test-Path "C:\IBMEC\01 - API com IA embarcada"

# Verificar cache
Test-Path "$env:USERPROFILE\.cache\huggingface"
```

Se retornar `False`, foi removido com sucesso!

---

**Desinstalação completa e fácil!** 🎉

