# FP&A Lab

Automação de relatórios financeiros usando Python e SQL para gerar gráficos e compilados mensais de forma escalável e organizada.

---

## 📋 Descrição

**FP&A Lab** é uma solução de automação para profissionais de planejamento e análise financeira que precisam gerar relatórios executivos e materiais para investidores de maneira eficiente e repetível.

O projeto implementa uma arquitetura modular onde cada gráfico ou relatório é uma **"migration"** (script independente), permitindo manutenção, teste e reutilização facilitados.

---

## 🎯 Objetivo

Gerar **gráficos e compilados mensais** para FP&A e investidores de forma:
- **Escalável**: arquitetura modular para adicionar novos relatórios facilmente
- **Organizada**: configurações centralizadas e fluxo de execução estruturado
- **Confiável**: tratamento de erros robusto e geração automática de logs

---

## 🏗️ Estrutura

A arquitetura segue um padrão modular com componentes bem definidos:

```
fpna-lab/
├── automation/          # Scripts de automação e orquestração
├── financial-analysis/  # Análises e transformações financeiras
├── sql/                 # Queries e modelos SQL
├── reports/             # Templates e configurações de relatórios
├── outputs/             # Arquivos gerados (imagens, Excel, etc.)
└── README.md            # Este arquivo
```

### Migrations
Cada gráfico/relatório é implementado como uma migration independente, permitindo:
- Execução isolada para teste
- Manutenção sem afetar outros relatórios
- Reutilização de componentes

### Orquestrador
Um orquestrador único:
- Executa todas as migrations em sequência
- Trata erros com graceful degradation
- Gera logs detalhados de execução

### Configurações Centralizadas
- Conexão com banco de dados
- Estilos visuais (cores, fontes, temas)
- Parâmetros de execução

---

## 🛠️ Tecnologias

- **Python** - Programação principal e orquestração
- **SQL** - Extração e transformação de dados
- **pandas** - Manipulação e análise de dados
- **matplotlib** - Visualização e geração de gráficos
- **SQLAlchemy** - ORM e gerenciamento de conexões

---

## 📦 Entregáveis

Os resultados de cada execução são armazenados em `outputs/`:
- 📊 **Imagens** - Gráficos em alta resolução (PNG, SVG)
- 📈 **Excel** - Compilados com dados brutos e formatação
- 📋 **Relatórios** - PDFs prontos para compartilhamento

Todos os arquivos estão organizados e prontos para análise e compartilhamento com stakeholders.

---

## 🚀 Como Usar

*(Instruções de instalação e execução em breve)*

---

**Repositório**: [ana-andressa/fpna-lab](https://github.com/ana-andressa/fpna-lab) 
