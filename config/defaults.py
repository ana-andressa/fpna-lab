"""
CONFIG PADRÕES: Formatação de Moeda, Data, Cores e Fontes

Edite este arquivo uma vez e use em todas as suas migrations!
"""

# ============================================================================
# FORMATAÇÃO DE MOEDA (R$)
# ============================================================================
CURRENCY_SYMBOL = "R$"
DECIMAL_SEPARATOR = ","        # 1.234,56
THOUSANDS_SEPARATOR = "."      # 1.234,56
PRECISION_DECIMALS = 2         # 2 casas decimais

def format_currency(value: float) -> str:
    """
    Formata valor para moeda brasileira
    Exemplo: 1234567.89 → "R$ 1.234.567,89"
    """
    formatted = f"{value:,.{PRECISION_DECIMALS}f}"
    # Swap: vírgula para decimal, ponto para milhares
    formatted = formatted.replace(",", "###TEMP###")
    formatted = formatted.replace(".", ",")
    formatted = formatted.replace("###TEMP###", ".")
    return f"{CURRENCY_SYMBOL} {formatted}"


def format_number(value: float, decimals: int = 0) -> str:
    """
    Formata número com separador de milhares
    Exemplo: 1234567 → "1.234.567"
    """
    formatted = f"{value:,.{decimals}f}"
    formatted = formatted.replace(",", "###TEMP###")
    formatted = formatted.replace(".", ",")
    formatted = formatted.replace("###TEMP###", ".")
    return formatted


# ============================================================================
# FORMATAÇÃO DE DATA
# ============================================================================
DATE_FORMAT = "%d/%m/%Y"  # 31/03/2025
DATE_MONTH_YEAR = "%b/%Y"  # Mar/2025


def format_date(date_obj) -> str:
    """Formata data para DD/MM/YYYY"""
    from datetime import datetime
    if isinstance(date_obj, str):
        date_obj = datetime.strptime(date_obj, "%Y-%m-%d")
    return date_obj.strftime(DATE_FORMAT)


# ============================================================================
# CORES DOS GRÁFICOS
# ============================================================================
COLORS = {
    "primary": "#1f77b4",       # Azul corporativo
    "secondary": "#ff7f0e",     # Laranja
    "success": "#2ca02c",       # Verde
    "warning": "#d62728",       # Vermelho
    "neutral": "#7f7f7f",       # Cinza
}

# Palheta de cores para múltiplos períodos
PALETTE_SEQUENTIAL = ["#1f77b4", "#aec7e8", "#ff7f0e", "#ffbb78"]


# ============================================================================
# TIPOGRAFIA E TAMANHOS
# ============================================================================
FONT_FAMILY = "sans-serif"
FONT_SIZE_TITLE = 16
FONT_SIZE_SUBTITLE = 13
FONT_SIZE_LABEL = 10
FONT_SIZE_TICK = 9


# ============================================================================
# TAMANHOS DE GRÁFICOS
# ============================================================================
FIGURE_SIZE_DEFAULT = (12, 6)      # Tamanho padrão
FIGURE_SIZE_LARGE = (15, 8)        # Gráfico grande
FIGURE_SIZE_SQUARE = (8, 8)        # Gráfico quadrado
DPI = 300                          # Resolução (alta qualidade)


# ============================================================================
# ESTILOS DE SAÍDA
# ============================================================================
OUTPUT_FORMAT = "png"              # Formato padrão (png, pdf, jpg)
OUTPUT_TRANSPARENT_BG = False      # Fundo branco vs transparente


# ============================================================================
# BANCO DE DADOS (será carregado de .env)
# ============================================================================
import os
from dotenv import load_dotenv

load_dotenv()

DB_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/dbname")
