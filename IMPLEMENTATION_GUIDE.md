# 🏗️ Guia de Implementação Passo a Passo

## ✅ O que foi criado para você

Sua estrutura FP&A Lab foi preparada com **padrões profissionais** baseados em:
- **Airflow** (orquestração)
- **dbt** (modelo de migrations)
- **Best practices** de Data Engineering e FP&A

### Estrutura de Pastas

```
fpna-lab/
├── 📄 run_migrations.py           ← EXECUTE ISTO para rodar tudo
├── 📄 QUICKSTART.py               ← Guia interativo
├── 📄 ARQUITETURA.md              ← Documentação completa
├── 📄 requirements.txt             ← Dependências Python
├── 📄 .env.example                ← Template de configuração
│
├── 📁 config/
│   └── defaults.py                ← Padrões visuais centralizados
│                                    (cores, fontes, datas, moedas)
│
├── 📁 lib/
│   ├── migration_base.py          ← Classe base para suas migrations
│   └── database.py                ← Gerenciador de conexão com BD
│
├── 📁 migrations/v1_reports/
│   └── 001_template_migration.py  ← COPIE ISTO para criar novas
│
├── 📁 queries/
│   ├── revenue_by_month.sql       ← Exemplo de query
│   └── (suas queries aqui)
│
├── 📁 outputs/                    ← Gráficos e Excel gerados
├── 📁 logs/                       ← Logs de execução
└── README.md                      ← Documentação principal
```

---

## 🎯 Passo 1: Setup Inicial (5 minutos)

### 1.1 Instalar Dependências

```bash
# Abra o terminal na pasta fpna-lab
cd fpna-lab

# Instale Python 3.8+ se não tiver

# Crie ambiente virtual
python -m venv venv
venv\Scripts\activate  # Windows
# ou source venv/bin/activate  # Mac/Linux

# Instale dependências
pip install -r requirements.txt
```

### 1.2 Configurar Banco de Dados

```bash
# Copie template de variáveis de ambiente
copy .env.example .env  # Windows
# ou cp .env.example .env  # Mac/Linux

# Abra .env em seu editor e preencha:
# DB_SERVER = seu servidor
# DB_NAME = seu banco de dados
# DB_USER = seu usuário
# DB_PASSWORD = sua senha
```

#### Exemplo .env preenchido:
```env
DB_DRIVER=ODBC Driver 17 for SQL Server
DB_SERVER=meu-servidor.database.windows.net
DB_NAME=financeiro_2025
DB_USER=ana_silva
DB_PASSWORD=minha_senha_segura
```

---

## 📊 Passo 2: Criar Primeira Migration (10 minutos)

### 2.1 Copiar Template

```bash
# Copie o file de template
copy migrations\v1_reports\001_template_migration.py migrations\v1_reports\003_meu_primeiro_relatorio.py
```

### 2.2 Editar Migration

Abra `migrations/v1_reports/003_meu_primeiro_relatorio.py` e adapte:

```python
from lib.migration_base import MigrationBase
from config import defaults
import pandas as pd
import matplotlib.pyplot as plt

class Migration003MeuPrimeiroRelatorio(MigrationBase):
    
    def get_name(self) -> str:
        # Nome único da migration
        return "003_meu_primeiro_relatorio"
    
    def execute(self) -> bool:
        try:
            # 1. CARREGAR DADOS
            self.log_info("Carregando dados do BD...")
            query = self.load_sql_query("meu_primeiro_relatorio")
            df = self.execute_query(query)
            
            if df.empty:
                self.log_warning("Nenhum dado encontrado")
                return False
            
            # 2. TRANSFORMAR (opcional)
            # df["data"] = pd.to_datetime(df["data"])
            
            # 3. GERAR GRÁFICO
            self.log_info("Gerando gráfico...")
            fig, ax = plt.subplots(figsize=defaults.FIGURE_SIZE_DEFAULT)
            
            ax.bar(df["mes"], df["valor"], color=defaults.COLORS["primary"])
            ax.set_title("Meu Primeiro Relatório", fontsize=defaults.FONT_SIZE_TITLE)
            ax.set_xlabel("Mês")
            ax.set_ylabel("Valor (R$)")
            
            # Formatter as labels com moeda
            for i, v in enumerate(df["valor"]):
                ax.text(i, v, defaults.format_currency(v), ha="center", va="bottom")
            
            # 4. SALVAR OUTPUT
            self.save_output("meu_primeiro_relatorio", fig)
            plt.close(fig)
            
            return True
        
        except Exception as e:
            self.log_error(f"Erro: {e}")
            return False
```

### 2.3 Criar Query SQL

Crie arquivo `queries/meu_primeiro_relatorio.sql`:

```sql
SELECT 
    FORMAT(data, 'MMM/yyyy') AS mes,
    SUM(valor) AS valor
FROM vendas
WHERE YEAR(data) = YEAR(GETDATE())
GROUP BY EOMONTH(data)
ORDER BY EOMONTH(data)
```

**DICA:** Teste a query no seu SSMS/DBeaver ANTES de usar na migration!

### 2.4 Executar

```bash
python run_migrations.py
```

**Saída esperada:**
```
======================================================================
INICIANDO ORQUESTRAÇÃO DE MIGRATIONS
Data/Hora: 01/04/2025 14:05:30
Total de migrations: 1
Stop on Error: False
======================================================================

[1/1] Executando: 003_meu_primeiro_relatorio
[INFO] Carregando dados do BD...
[INFO] Dados carregados com sucesso. Registros: 12
[INFO] Gerando gráfico...
[INFO] Salvando gráfico...
✓ SUCESSO: 003_meu_primeiro_relatorio
Tempo de execução: 2.34s

...
✓ Sucesso: 1
✗ Falhas: 0
Tempo total: 2.34s
```

Seu gráfico estará em: `outputs/003_meu_primeiro_relatorio_Apr2025.png`

---

## 🎨 Passo 3: Personalizar Padrões Visuais (5 minutos)

Abra `config/defaults.py` e customize para sua empresa:

### Alterar Cores

```python
COLORS = {
    "primary": "#1f77b4",       # Azul corporativo
    "secondary": "#ff7f0e",     # Laranja
    "success": "#2ca02c",       # Verde
    "warning": "#d62728",       # Vermelho
}
```

### Alterar Fonte

```python
FONT_FAMILY = "Arial"  # ou "Times New Roman", "Helvetica"
FONT_SIZE_TITLE = 18   # Aumentar tamanho
```

### Alterar Formatação de Moeda

```python
CURRENCY_SYMBOL = "R$"  # ou "USD", "EUR"
PRECISION_DECIMALS = 2  # Casas decimais
```

**BENEFÍCIO:** Uma única mudança afeta TODOS os gráficos! 🎯

---

## 📈 Passo 4: Criar Mais Migrations (repetir Passo 2)

Agora que você sabe como funciona, pode criar quantas quiser:

```bash
# 004_graph_cashflow.py
# 005_compile_dre.py
# 006_analysis_expenses.py
# ...
```

**Convenção de nomes:**
- `00X_graph_*` para gráficos
- `00X_compile_*` para compilados (Excel)
- `00X_analysis_*` para análises

---

## 🔄 Passo 5: Agendar Execução Automática

### Windows (Task Scheduler)

1. Abra **Task Scheduler**
2. Crie nova tarefa
3. Aba **Geral**: Dê um nome (ex: "FP&A Lab Daily")
4. Aba **Acionadores**: Defina para rodar diariamente (ex: 8:00 AM)
5. Aba **Ações**:
   - Ação: `Iniciar um programa`
   - Programa: `C:\Python39\python.exe` (seu caminho do Python)
   - Argumentos: `C:\Users\User\fpna-lab\run_migrations.py`
   - Pasta de início: `C:\Users\User\fpna-lab`

6. Clique **OK**

Pronto! Suas migrations rodarão automaticamente todo dia.

### Linux/Mac (Cron)

```bash
# Editar crontab
crontab -e

# Adicionar linha (executa todo dia às 8:00 AM):
0 8 * * * cd /home/user/fpna-lab && /usr/bin/python3 run_migrations.py
```

---

## 🐛 Passo 6: Solucionar Problemas

### Erro: "ModuleNotFoundError: No module named 'sqlalchemy'"

```bash
# Instale novamente as dependências
pip install -r requirements.txt
```

### Erro: "Could not connect to database"

```bash
# Verifique .env
cat .env
# Confirme credenciais e que BD está acessível
```

### Erro: "Query returned no results"

```bash
# Teste a query direto no seu BD (SSMS, DBeaver)
# Confirme que há dados para o período
# Verifique os parâmetros
```

### Uma migration falhou, outras continuaram?

✅ **Isso é ESPERADO!** É o isolamento de erro funcionando.

Verifique os logs:
```bash
# Último log
cat logs\run_*.log

# Relatório estruturado
cat logs\report_*.json
```

---

## 📋 Checklist de Implementação

- [ ] Python 3.8+ instalado
- [ ] Dependências instaladas (`pip install -r requirements.txt`)
- [ ] Arquivo `.env` criado e preenchido com credenciais
- [ ] Query SQL testada no seu BD
- [ ] Migration criada e copiada
- [ ] `python run_migrations.py` executado com sucesso
- [ ] Arquivo gerado em `outputs/`
- [ ] Estilos em `config/defaults.py` personalizados

---

## 🚀 Próximas Melhorias

Depois de ter o básico funcionando, considere:

- ✅ Conectar ao BD em produção (em vez de dev)
- ✅ Adicionar mais migrations para todos seus relatórios
- ✅ Agendar execução automática
- ✅ Integrar com Microsoft Teams/Slack para notificações
- ✅ Adicionar validações de dados (data quality checks)
- ✅ Criar dashboard de monitoramento dos logs

---

## 📞 Referência Rápida de Comandos

```bash
# Instalar dependências
pip install -r requirements.txt

# Executar todas as migrations
python run_migrations.py

# Ver último log
type logs\run_*.log

# Ver estrutura de pastas
tree /F

# Ativar ambiente virtual
venv\Scripts\activate

# Desativar ambiente virtual
deactivate
```

---

**Parabéns! Você tem um sistema profissional, escalável e automatizado para FP&A! 🎉**

