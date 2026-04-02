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
# CORES PADRÃO
# ============================================================================
# ── Base ──────────────────────────────────────────
COLORS = {
    "primary":   "#1f77b4",  # Azul corporativo — links, destaques, série 1
    "secondary": "#ff7f0e",  # Laranja — acento, alertas leves
    "success":   "#2ca02c",  # Verde — positivo, crescimento
    "warning":   "#d62728",  # Vermelho — negativo, queda
    "neutral":   "#7f7f7f",  # Cinza — labels, elementos secundários
}

# ── Texto ────────────────────────────────────
TEXT_COLORS = {
    "text_primary":   "#1a1a2e",  # Títulos e corpo principal
    "text_secondary": "#4a5568",  # Subtítulos, rótulos
    "text_muted":     "#9aa3b0",  # Notas, placeholders, disclaimers
    "text_inverse":   "#ffffff",  # Texto sobre fundo escuro
}

def get_color(name: str, default: str = None) -> str:
    """Retorna cor a partir do nome, com fallback opcional."""
    if name in COLORS:
        return COLORS[name]
    if default is not None:
        return default
    raise KeyError(f"Cor não encontrada: {name}")


# ── Gráficos ─────────────────────────────────────
CHART_COLORS = {
    "chart_1":  get_color("primary"),   # Série principal (herda primary)
    "chart_2":  get_color("secondary"), # Série 2 (herda secondary)
    "chart_3":  get_color("success"),   # Série positiva
    "chart_4":  get_color("warning"),   # Série negativa
    "chart_5":  "#9467bd",              # Série extra (roxo neutro)
    "chart_bg": "#f9fafb",              # Background do gráfico
}

# ── Tabelas ──────────────────────────────────────
TABLE_COLORS = {
    "table_header":    get_color("primary"),  # Cabeçalho (herda primary)
    "table_row_even":  "#f0f4f8",             # Zebra — linha par
    "table_row_odd":   "#ffffff",             # Zebra — linha ímpar
    "table_border":    "#e2e8f0",             # Dividers
    "table_highlight": "#fff3cd",             # Linha de destaque (ex: total)
}

# Paleta de cores para múltiplos períodos
PALETTE_SEQUENTIAL = [get_color("primary"), "#aec7e8", get_color("secondary"), "#ffbb78"]


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
