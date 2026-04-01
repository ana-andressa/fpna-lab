"""
TEMPLATE: Use como base para criar suas migrations

Passos para usar:
1. Copie este arquivo: cp migrations/template.py migrations/001_seu_relatorio.py
2. Renomeie a função
3. Implemente sua lógica (carregar BD → transformar → gerar saída)
4. Execute: python run_migrations.py
"""

import pandas as pd
import matplotlib.pyplot as plt
from config.defaults import format_currency, format_number, COLORS, FONT_SIZE_TITLE


def migration_template():
    """
    TEMPLATE DE MIGRATION
    
    Edite este arquivo e implemente sua lógica aqui.
    """
    
    print("=" * 70)
    print("MIGRATION: Template")
    print("=" * 70)
    
    try:
        # ====================================================================
        # PASSO 1: CARREGAR DADOS DO BANCO DE DADOS
        # ====================================================================
        print("📊 Carregando dados...")
        
        # Descomente e adapte para seu BD:
        # from sqlalchemy import create_engine
        # from config.defaults import DB_URL
        # 
        # engine = create_engine(DB_URL)
        # query = "SELECT mes, valor FROM vendas WHERE ano = 2025"
        # df = pd.read_sql(query, engine)
        
        # Para teste, usar dados mock:
        df = pd.DataFrame({
            "mes": ["Jan", "Fev", "Mar", "Abr", "Mai"],
            "valor": [100000, 120000, 95000, 150000, 130000]
        })
        
        print(f"✓ {len(df)} registros carregados")
        
        # ====================================================================
        # PASSO 2: TRANSFORMAR DADOS (opcional)
        # ====================================================================
        print("🔄 Transformando dados...")
        
        # Exemplo: adicionar coluna calculada
        df["valor_formatado"] = df["valor"].apply(format_currency)
        
        print("✓ Dados transformados")
        
        # ====================================================================
        # PASSO 3: GERAR SAÍDA (gráfico OU Excel)
        # ====================================================================
        
        # OPÇÃO A: Graphico
        print("📈 Gerando gráfico...")
        fig, ax = plt.subplots(figsize=(12, 6))
        
        ax.bar(df["mes"], df["valor"], color=COLORS["primary"], alpha=0.8)
        ax.set_title("Receita por Mês", fontsize=FONT_SIZE_TITLE, fontweight="bold")
        ax.set_xlabel("Período")
        ax.set_ylabel("Faturamento (R$)")
        
        # Adicionar valores nas barras
        for i, v in enumerate(df["valor"]):
            ax.text(i, v, format_currency(v), ha="center", va="bottom", fontsize=9)
        
        fig.tight_layout()
        
        # ====================================================================
        # PASSO 4: SALVAR SAÍDA
        # ====================================================================
        print("💾 Salvando arquivo...")
        
        # Opção A: Salvar gráfico
        output_path = "outputs/template_graph.png"
        fig.savefig(output_path, dpi=300, bbox_inches="tight")
        print(f"✓ Gráfico salvo em: {output_path}")
        
        plt.close(fig)
        
        # Opção B: Salvar Excel (descomente para usar)
        # output_path = "outputs/template_data.xlsx"
        # df.to_excel(output_path, index=False)
        # print(f"✓ Excel salvo em: {output_path}")
        
        # ====================================================================
        # SUCESSO
        # ====================================================================
        print("=" * 70)
        print("✓ MIGRATION CONCLUÍDA COM SUCESSO")
        print("=" * 70)
        return True
    
    except Exception as e:
        print("=" * 70)
        print(f"✗ ERRO NA MIGRATION: {e}")
        print("=" * 70)
        import traceback
        traceback.print_exc()
        return False


# ============================================================================
# COMO CRIAR SUAS MIGRATIONS
# ============================================================================
"""
1. COPIE este arquivo:
   cp migrations/template.py migrations/001_receita_mensal.py

2. RENOMEIE a função:
   def migration_template():
   ↓
   def migration_001_receita_mensal():

3. IMPLEMENTE sua lógica:
   - Copie a query do seu BD
   - Adapte o código
   - Teste localmente

4. SALVE e execute:
   python run_migrations.py

5. VEJA resultado em outputs/

EXEMPLO PRONTO DE OUTRAS MIGRATIONS:

### Para Gráfico:
    fig, ax = plt.subplots()
    ax.plot(df['mes'], df['valor'], color=COLORS['primary'])
    fig.savefig('outputs/seu_grafico.png')

### Para Excel:
    df.to_excel('outputs/seu_compilado.xlsx', index=False)

### Para Usar Padrões:
    valor = format_currency(12345.67)  # "R$ 12.345,67"
    numero = format_number(98765)      # "98.765"
    cor = COLORS['success']             # "#2ca02c"
"""

if __name__ == "__main__":
    migration_template()
