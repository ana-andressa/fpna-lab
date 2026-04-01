# FP&A Lab

> Automação inteligente de relatórios financeiros. Gere gráficos e compilados mensais com um único comando.

---

## 🎯 O que você consegue fazer

| | |
|:---|:---|
| 📊 **Gráficos Profissionais** | Visualizações em alta resolução (PNG) com padrões corporativos |
| 📈 **Compilados Excel** | Planilhas formatadas e prontas para compartilhamento |
| 🔄 **Automação Completa** | Execute todos os relatórios de uma vez |
| ⚙️ **Padrões Centralizados** | Moeda, datas, cores e estilos consistentes em tudo |
| 🎨 **Facilmente Customizável** | Edite padrões uma vez, afeta todos os relatórios |

---

## ⚡ Como Funciona

```bash
# 1. Criar um relatório (copiar template)
cp migrations/template.py migrations/001_seu_relatorio.py

# 2. Implementar sua lógica (carregar BD → processar → salvar)

# 3. Executar tudo automaticamente
python run_migrations.py

# Resultado: seus gráficos/Excel em outputs/
```

---

## 📁 Arquitetura Limpa

```
fpna-lab/
├── config/defaults.py           Padrões visuais (moeda, cores, datas)
├── migrations/                  Seus relatórios aqui
├── run_migrations.py            Orquestrador
└── outputs/                     Seus arquivos gerados
```

**Conceito:** Cada gráfico/compilado é uma migration independente. Se uma quebra, as outras continuam funcionando.

---

## 🛠️ Stack Tecnológico

- **Python 3.8+** - Linguagem principal
- **PostgreSQL** - Banco de dados
- **pandas** - Análise de dados
- **matplotlib** - Visualização
- **SQLAlchemy** - Conexão com BD

---

## 💡 Principais Características

✅ **Modular** - Cada relatório é independente  
✅ **Escalável** - Adicione novos sem quebrar existentes  
✅ **Confiável** - Isolamento de erro automático  
✅ **Profissional** - Padrões de formatação corporativos  
✅ **Rápido** - Gere múltiplos relatórios em segundos  

---

## 📚 Documentação

- **[Guia Completo](DOCUMENTACAO.md)** - Setup, exemplos, troubleshooting
- **[Padrões Visuais](config/defaults.py)** - Moeda, cores, fontes, datas

---

## 🚀 Comece Agora

```bash
# 1. Instalar dependências
pip install -r requirements.txt

# 2. Configurar banco de dados
cp .env.example .env
# Edite .env com suas credenciais

# 3. Criar primeira migration
cp migrations/template.py migrations/001_seu_relatorio.py

# 4. Executar
python run_migrations.py
```

**[Ver documentação para instruções detalhadas →](DOCUMENTACAO.md)**

---

**Repositório:** [ana-andressa/fpna-lab](https://github.com/ana-andressa/fpna-lab) 
