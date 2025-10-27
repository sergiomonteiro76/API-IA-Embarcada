# ⚡ Instalação Super Simples - Windows

## 🎯 Apenas 3 Comandos!

Abra o **PowerShell** na pasta do projeto e execute:

```powershell
# 1️⃣ Criar ambiente virtual
python -m venv venv

# 2️⃣ Ativar ambiente virtual
.\venv\Scripts\Activate.ps1

# 3️⃣ Instalar tudo
pip install flask transformers torch

pip install tf-keras
```

**Pronto!** Agora execute:

```powershell
python app.py
```

Acesse: **http://localhost:5000**

---

## 🗑️ Como Desinstalar Tudo

```powershell
# 1. Desativar ambiente virtual
deactivate

# 2. Fechar o PowerShell

# 3. Deletar a pasta do projeto
# (Isso remove TUDO - aplicação e modelos)
```

Os modelos ficam em cache em:
```
C:\Users\SeuUsuario\.cache\huggingface\
```

Para liberar espaço, delete esta pasta também.

---

## ❓ Problemas?

### Erro: "Activate.ps1 cannot be loaded"

**Solução:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Erro: "python não é reconhecido"

**Solução:** Use `py` ao invés de `python`:
```powershell
py -m venv venv
py app.py
```

### Download lento?

**Normal!** Na primeira vez, vai baixar ~100MB de modelos.  
Nas próximas vezes, carrega do cache (rápido).

---

## 💡 Dicas

- **Primeira execução:** 2-3 minutos de download
- **Próximas execuções:** ~10 segundos para carregar
- **Funciona offline:** Após o primeiro download
- **Tamanho total:** ~500MB (aplicação + modelos)

---

**É isso! Simples assim!** 🚀

