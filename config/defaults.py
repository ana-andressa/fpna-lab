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
# TIPOGRAFIA: ESTRUTURA ORGANIZADA POR CONTEXTO
# ============================================================================

# Base: Famílias de fontes
TYPOGRAPHY_FAMILIES = {
    "display": "Poppins",       # Títulos e destaques
    "body": "Calibri",          # Texto corpo e dados
}

# Tamanhos base
TYPOGRAPHY_SIZES = {
    "xs": 8,                    # Rodapé, notas
    "sm": 9,                    # Eixos de gráficos, tabelas
    "md": 11,                   # Rótulos, legenda
    "lg": 12,                   # Subtítulos
    "xl": 16,                   # Títulos principais
}

# Estilos compostos por contexto de uso
TYPOGRAPHY_STYLES = {
    "title": {
        "font_family": TYPOGRAPHY_FAMILIES["display"],
        "font_size": TYPOGRAPHY_SIZES["xl"],
        "font_weight": "bold",
        # Uso: Títulos principais de gráficos e relatórios
    },
    "subtitle": {
        "font_family": TYPOGRAPHY_FAMILIES["display"],
        "font_size": TYPOGRAPHY_SIZES["lg"],
        "font_weight": "normal",
        # Uso: Subtítulos e seções secundárias
    },
    "label": {
        "font_family": TYPOGRAPHY_FAMILIES["body"],
        "font_size": TYPOGRAPHY_SIZES["md"],
        "font_weight": "normal",
        # Uso: Rótulos de eixo, legenda de gráficos
    },
    "tick": {
        "font_family": TYPOGRAPHY_FAMILIES["body"],
        "font_size": TYPOGRAPHY_SIZES["sm"],
        "font_weight": "normal",
        # Uso: Valores nos eixos de gráficos
    },
    "table": {
        "font_family": TYPOGRAPHY_FAMILIES["body"],
        "font_size": TYPOGRAPHY_SIZES["sm"],
        "font_weight": "normal",
        # Uso: Conteúdo de tabelas
    },
    "caption": {
        "font_family": TYPOGRAPHY_FAMILIES["body"],
        "font_size": TYPOGRAPHY_SIZES["sm"],
        "font_weight": "normal",
        "font_style": "italic",
        "color": COLORS["neutral"],
        # Uso: Descrição/legenda abaixo de título ou gráfico
    },
}


# ============================================================================
# TAMANHOS DE GRÁFICOS (em polegadas)
# ============================================================================
# Proporções baseadas em layouts Word típicos
FIGURE_SIZE_SMALL = (10, 6)        # Gráfico pequeno/compacto (~14cm x 7,6cm em Word)
FIGURE_SIZE_MEDIUM = (13, 5.5)     # Gráfico médio - largo e curto (~17,3cm x 6,9cm em Word)
FIGURE_SIZE_DEFAULT = (12, 6)      # Tamanho padrão (alternativa balanceada)
FIGURE_SIZE_LARGE = (15, 8.5)      # Gráfico grande (~17,5cm x 9,8cm em Word)
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
# Configuração: Crie um arquivo .env na raiz com DATABASE_URL=postgresql://...
# O .env fica LOCAL (não commitado no GitHub). Seguro!

import os
from dotenv import load_dotenv

load_dotenv()

DB_URL = os.getenv("DATABASE_URL")
if not DB_URL:
    raise ValueError("DATABASE_URL não configurada no arquivo .env")
