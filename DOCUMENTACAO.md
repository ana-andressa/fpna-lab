# 📚 DOCUMENTAÇÃO - FP&A Lab

## Índice
1. [Visão Geral](#visão-geral)
2. [Estrutura do Projeto](#estrutura-do-projeto)
3. [Configuração Inicial](#configuração-inicial)
4. [Como Criar Uma Migration](#como-criar-uma-migration)
5. [Usando Padrões](#usando-padrões)
6. [Exemplos Práticos](#exemplos-práticos)
7. [Solução de Problemas](#solução-de-problemas)

---

## Visão Geral

**FP&A Lab** é um sistema para **automatizar relatórios financeiros** usando Python + PostgreSQL.

### O que ele faz:
- ✅ Executa múltiplas migrations (gráficos, compilados Excel)
- ✅ Busca dados do banco PostgreSQL
- ✅ Aplica formatação padrão (moeda R$, data DD/MM/YYYY)
- ✅ Gera outputs prontos (PNG, XLSX)
- ✅ Se uma quebra, as outras continuam

### Caso de Uso:
Você tem **5 relatórios diferentes** que precisa gerar todo mês. Ao invés de fazer manualmente, o FP&A Lab faz tudo automaticamente de uma vez:

```bash
python run_migrations.py
# Gera os 5 relatórios em segundos
```

---

## Estrutura do Projeto

```
fpna-lab/
│
├── config/
│   ├── __init__.py              (deixe vazio)
│   └── defaults.py              ← PADRÕES VISUAIS
│
├── migrations/
│   ├── template.py              ← TEMPLATE PARA COPIAR
│   ├── 001_receita_mensal.py    ← SUA PRIMEIRA MIGRATION
│   └── 002_dre_consolidado.py   ← SUA SEGUNDA MIGRATION
│
├── run_migrations.py            ← EXECUTE ISTO
├── requirements.txt             ← DEPENDÊNCIAS
├── .env.example                 ← TEMPLATE DE CONFIG
├── .env                         ← SUA CONFIG (não commitar)
│
├── outputs/                     ← RESULTADOS AQUI
│   ├── receita_mensal.png
│   └── dre_consolidado.xlsx
│
└── README.md
```

---

## Configuração Inicial

### Passo 1: Instalar Python e Dependências

**Pré-requisito:** Python 3.8+

```bash
# Instalar dependências
pip install -r requirements.txt
```

### Passo 2: Configurar Banco de Dados

```bash
# Copiar template
cp .env.example .env
```

Edite `.env` com suas credenciais:

```env
DATABASE_URL=postgresql://seu_usuario:sua_senha@localhost:5432/seu_banco
```

**Exemplo real:**
```env
DATABASE_URL=postgresql://ana_silva:minha_senha123@meu-server.com:5432/financeiro_2025
```

> **IMPORTANTE:** `.env` já está em `.gitignore`, não será commitado no Git ✓

### Passo 3: Testar Conexão

Abra um terminal Python e teste:

```python
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()
engine = create_engine(os.getenv("DATABASE_URL"))
print("✓ Conexão OK!" if engine else "✗ Erro na conexão")
```

---

## Como Criar Uma Migration

### Padrão de Nomes

Use este padrão para nomear suas migrations:

```
NNN_tipo_nome.py

NNN = número sequencial (001, 002, 003...)
tipo = graph (gráfico) ou compile (Excel)
nome = descrição breve

Exemplos:
✓ 001_graph_receita_mensal.py
✓ 002_compile_dre.py
✓ 003_graph_cashflow.py
```

### Passos para Criar

#### Passo 1: Copiar Template

```bash
cp migrations/template.py migrations/001_seu_relatorio.py
```

#### Passo 2: Editar Nome da Função

Abra `001_seu_relatorio.py` e altere:

```python
# DE:
def migration_template():

# PARA:
def migration_001_seu_relatorio():
```

#### Passo 3: Implementar Lógica

```python
def migration_001_receita_mensal():
    """Gráfico de Receita por Mês"""
    
    print("=" * 70)
    print("MIGRATION: 001 - Receita Mensal")
    print("=" * 70)
    
    try:
        # 1. CARREGAR DADOS
        print("📊 Carregando dados...")
        
        from sqlalchemy import create_engine
        import os
        from dotenv import load_dotenv
        
        load_dotenv()
        engine = create_engine(os.getenv("DATABASE_URL"))
        
        query = """
        SELECT 
            TO_CHAR(data, 'Mon') AS mes,
            SUM(valor) AS receita
        FROM vendas
        WHERE EXTRACT(YEAR FROM data) = EXTRACT(YEAR FROM NOW())
        GROUP BY TO_CHAR(data, 'Mon'), EXTRACT(MONTH FROM data)
        ORDER BY EXTRACT(MONTH FROM data)
        """
        
        df = pd.read_sql(query, engine)
        print(f"✓ {len(df)} registros carregados")
        
        # 2. GERAR GRÁFICO
        print("📈 Gerando gráfico...")
        
        from config.defaults import format_currency, COLORS, FONT_SIZE_TITLE
        import matplotlib.pyplot as plt
        
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.bar(df["mes"], df["receita"], color=COLORS["primary"], alpha=0.8)
        ax.set_title("Receita por Mês", fontsize=FONT_SIZE_TITLE, fontweight="bold")
        ax.set_xlabel("Período")
        ax.set_ylabel("Faturamento (R$)")
        
        # Adicionar valores nas barras
        for i, v in enumerate(df["receita"]):
            ax.text(i, v, format_currency(v), ha="center", va="bottom", fontsize=9)
        
        fig.tight_layout()
        
        # 3. SALVAR
        print("💾 Salvando arquivo...")
        output_path = "outputs/001_receita_mensal.png"
        fig.savefig(output_path, dpi=300, bbox_inches="tight")
        print(f"✓ Gráfico salvo em: {output_path}")
        
        plt.close(fig)
        
        print("=" * 70)
        print("✓ MIGRATION CONCLUÍDA COM SUCESSO")
        print("=" * 70)
        return True
    
    except Exception as e:
        print("=" * 70)
        print(f"✗ ERRO: {e}")
        print("=" * 70)
        import traceback
        traceback.print_exc()
        return False
```

#### Passo 4: Executar

```bash
python run_migrations.py
```

**Resultado esperado:**
```
🔍 Procurando migrations em migrations/...
  ✓ Encontrada: 001_seu_relatorio.py

📊 Total de migrations: 1

[1/1] 001_seu_relatorio.py
----------------------------------------------------------------------
======================================================================
MIGRATION: 001 - Receita Mensal
======================================================================
📊 Carregando dados...
✓ 12 registros carregados
📈 Gerando gráfico...
💾 Salvando arquivo...
✓ Gráfico salvo em: outputs/001_receita_mensal.png
======================================================================
✓ MIGRATION CONCLUÍDA COM SUCESSO
======================================================================

======================================================================
RESUMO DE EXECUÇÃO
======================================================================
✓ Sucesso: 1/1
✗ Falhas: 0/1
⏱️  Tempo total: 2.34s
======================================================================

🎉 TODAS AS MIGRATIONS EXECUTADAS COM SUCESSO!
📊 Outputs salvos em: outputs/
```

---

## Usando Padrões

Arquivo: `config/defaults.py`

### Formatação de Moeda

```python
from config.defaults import format_currency

# Entrada: 1234567.89
# Saída: "R$ 1.234.567,89"

valor = format_currency(1234567.89)
print(valor)  # R$ 1.234.567,89
```

### Formatação de Número

```python
from config.defaults import format_number

# Entrada: 1234567
# Saída: "1.234.567"

numero = format_number(1234567)
print(numero)  # 1.234.567
```

### Usando Cores

```python
from config.defaults import COLORS

# Cores disponíveis:
COLORS["primary"]    # "#1f77b4" (azul)
COLORS["secondary"]  # "#ff7f0e" (laranja)
COLORS["success"]    # "#2ca02c" (verde)
COLORS["warning"]    # "#d62728" (vermelho)
COLORS["neutral"]    # "#7f7f7f" (cinza)

# Em um gráfico:
ax.bar(x, y, color=COLORS["primary"])
```

### Tamanhos de Fonte

```python
from config.defaults import FONT_SIZE_TITLE, FONT_SIZE_LABEL, FONT_SIZE_TICK

ax.set_title("Meu Título", fontsize=FONT_SIZE_TITLE)         # 16
ax.set_ylabel("Label", fontsize=FONT_SIZE_LABEL)             # 10
ax.tick_params(labelsize=FONT_SIZE_TICK)                     # 9
```

### Tamanhos de Gráfico

```python
from config.defaults import FIGURE_SIZE_DEFAULT, FIGURE_SIZE_LARGE, DPI

# Padrão
fig, ax = plt.subplots(figsize=FIGURE_SIZE_DEFAULT)  # (12, 6)

# Grande
fig, ax = plt.subplots(figsize=FIGURE_SIZE_LARGE)    # (15, 8)

# Resolução
fig.savefig("output.png", dpi=DPI)  # 300 DPI (alta qualidade)
```

---

## Exemplos Práticos

### Exemplo 1: Gráfico de Barras (Receita por Mês)

```python
def migration_001_receita_mensal():
    import pandas as pd
    import matplotlib.pyplot as plt
    from sqlalchemy import create_engine
    import os
    from dotenv import load_dotenv
    from config.defaults import format_currency, COLORS, FONT_SIZE_TITLE, FIGURE_SIZE_DEFAULT, DPI
    
    load_dotenv()
    engine = create_engine(os.getenv("DATABASE_URL"))
    
    # Carregar dados
    query = "SELECT mes, receita FROM vendas_por_mes WHERE ano = 2025"
    df = pd.read_sql(query, engine)
    
    # Gerar gráfico
    fig, ax = plt.subplots(figsize=FIGURE_SIZE_DEFAULT)
    ax.bar(df["mes"], df["receita"], color=COLORS["primary"])
    ax.set_title("Receita por Mês", fontsize=FONT_SIZE_TITLE)
    
    # Salvar
    fig.savefig("outputs/001_receita.png", dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    
    return True
```

### Exemplo 2: Gráfico de Linha (Lucro Acumulado)

```python
def migration_002_lucro_acumulado():
    import pandas as pd
    import matplotlib.pyplot as plt
    from sqlalchemy import create_engine
    import os
    from dotenv import load_dotenv
    from config.defaults import format_currency, COLORS, FIGURE_SIZE_DEFAULT, DPI
    
    load_dotenv()
    engine = create_engine(os.getenv("DATABASE_URL"))
    
    # Carregar dados
    query = "SELECT mes, lucro_acumulado FROM lucro_mensal WHERE ano = 2025"
    df = pd.read_sql(query, engine)
    
    # Gerar gráfico
    fig, ax = plt.subplots(figsize=FIGURE_SIZE_DEFAULT)
    ax.plot(df["mes"], df["lucro_acumulado"], marker="o", color=COLORS["success"], linewidth=2)
    ax.fill_between(range(len(df)), df["lucro_acumulado"], alpha=0.3, color=COLORS["success"])
    ax.set_title("Lucro Acumulado", fontsize=FONT_SIZE_TITLE)
    
    fig.savefig("outputs/002_lucro_acumulado.png", dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    
    return True
```

### Exemplo 3: Compilado Excel (DRE)

```python
def migration_003_dre_mensal():
    import pandas as pd
    from sqlalchemy import create_engine
    import os
    from dotenv import load_dotenv
    from config.defaults import format_currency
    
    load_dotenv()
    engine = create_engine(os.getenv("DATABASE_URL"))
    
    # Carregar dados
    query = "SELECT departamento, receita, custos, despesas FROM dre WHERE mes = 3 AND ano = 2025"
    df = pd.read_sql(query, engine)
    
    # Transformar
    df["receita_fmt"] = df["receita"].apply(format_currency)
    df["custos_fmt"] = df["custos"].apply(format_currency)
    df["despesas_fmt"] = df["despesas"].apply(format_currency)
    
    # Selecionar colunas
    df_export = df[["departamento", "receita_fmt", "custos_fmt", "despesas_fmt"]]
    df_export.columns = ["Departamento", "Receita", "Custos", "Despesas"]
    
    # Salvar Excel
    output_path = "outputs/003_dre_mensal.xlsx"
    df_export.to_excel(output_path, index=False)
    
    return True
```

---

## Solução de Problemas

### Erro: "ModuleNotFoundError: No module named 'sqlalchemy'"

```bash
# Solução: Instalar dependências novamente
pip install -r requirements.txt
```

### Erro: "Could not connect to database"

**Possíveis causas:**

1. **Credenciais incorretas em `.env`**
   ```bash
   # Testar conexão
   psql -h seu_host -U seu_usuario -d seu_banco
   ```

2. **Banco não acessível**
   - Verificar firewall
   - Testar conexão em outro programa (DBeaver, pgAdmin)

3. **DATABASE_URL formatado errado**
   ```
   ✓ Correto: postgresql://user:pass@host:5432/database
   ✗ Errado: PostgreSQL://user:pass@host:5432/database (maiúscula)
   ```

### Erro: "Query returned no results"

1. Testar query direto no banco:
   ```sql
   SELECT * FROM sua_tabela WHERE ano = 2025;
   ```

2. Verificar se tabela existe e tem dados

### Error: "No function migration_* found"

Verifique se o nome da função está correto:

```python
# ✓ Correto (começa com migration_)
def migration_001_receita():
    pass

# ✗ Errado
def meu_relatorio():
    pass
```

### Gráfico não aparece ou está vazio

```python
# Adicione debug:
print(f"Registros: {len(df)}")
print(df.head())  # Ver primeiras linhas

# Verifique se os dados estão corretos:
print(df.dtypes)  # Ver tipos de dados
```

---

## Dica Final: Criar Múltiplas Migrations

Repita o processo para cada relatório:

```bash
# Migration 1
cp migrations/template.py migrations/001_graph_receita.py
# Edite e implemente

# Migration 2  
cp migrations/template.py migrations/002_compile_dre.py
# Edite e implemente

# Migration 3
cp migrations/template.py migrations/003_graph_cashflow.py
# Edite e implemente

# Executar TODAS
python run_migrations.py
```

Todas serão executadas em ordem sequencial (001, 002, 003...) e se uma falhar, as outras continuam! 🎯

