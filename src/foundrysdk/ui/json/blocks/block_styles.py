
# ============================================================
# STYLING CONSTANTS
# ============================================================

# Colors
OUTLINES = {
    "object":  "#367FC2",
    "array":   "#9862D4",
    "string":  "#32A875",
    "number":  "#D99138",
    "boolean": "#D45B7B",
    "null":    "#858C9C",
}

COLORS = {
    "object":  "#1A3048",
    "array":   "#3D2855",
    "string":  "#1A4030",
    "number":  "#593516",
    "boolean": "#572638",
    "null":    "#363A43",
}

TEXT_COLOR = "#FFFFFF"
TRANSPARENT = "transparent"

# Borders
BORDER_WIDTH = 1

VARIABLE_BORDER_RADIUS = 5
VALUE_BORDER_RADIUS = 7
CONTAINER_BORDER_RADIUS = 10
BUTTON_BORDER_RADIUS = 5

# Fonts
FONT_SIZE = 14
FONT_WEIGHT_BOLD = "bold"
CONTAINER_COUNT_FONT_SIZE = 12

# Padding
VARIABLE_PADDING = "5px 8px"
BUTTON_PADDING = "4px 9px"
KEY_PADDING = "2px 2px"

# Layout margins
VARIABLE_MARGINS = (2, 0, 2, 0)
KEY_MARGINS = (2, 0, 2, 0)
VALUE_MARGINS = (12, 4, 4, 4)
CONTAINER_MARGINS = (10, 8, 10, 10)
CHILDREN_MARGINS = (12, 8, 12, 8)
ROOT_MARGINS = (0, 0, 0, 0)

# Layout spacing
VALUE_SPACING = 10
CONTAINER_SPACING = 7
ROOT_SPACING = 0

# Widget dimensions
TOGGLE_BUTTON_WIDTH = 28

# Button states
BUTTON_HOVER_BACKGROUND = None


# ============================================================
# STYLESHEET HELPERS
# ============================================================

def key_style():
    return f"""
        QFrame {{
            background: {TRANSPARENT};
            border: none;
        }}

        QLineEdit {{
            color: {TEXT_COLOR};
            background: {TRANSPARENT};
            border: none;
            outline: none;
            padding: {KEY_PADDING};
            font-size: {FONT_SIZE}px;
            font-weight: {FONT_WEIGHT_BOLD};
        }}
    """

def variable_style(kind):
    return f"""
        QFrame {{
            background: {COLORS[kind]};
            border: {BORDER_WIDTH}px solid {OUTLINES[kind]};
            border-radius: {VARIABLE_BORDER_RADIUS}px;
        }}

        QLineEdit {{
            color: {TEXT_COLOR};
            background: {TRANSPARENT};
            border: none;
            padding: {VARIABLE_PADDING};
        }}
    """

def value_style(kind):
    return f"""
        QFrame {{
            background: {TRANSPARENT};
            border: {BORDER_WIDTH}px solid {OUTLINES[kind]};
            border-radius: {VALUE_BORDER_RADIUS}px;
        }}

        QLabel {{
            font-size: {FONT_SIZE}px;
            color: {TEXT_COLOR};
            background: {TRANSPARENT};
            border: none;
        }}
    """


def container_style(kind):
    hover_background = BUTTON_HOVER_BACKGROUND or OUTLINES[kind]

    return f"""
        QFrame {{
            background: {TRANSPARENT};
            border: {BORDER_WIDTH}px solid {OUTLINES[kind]};
            border-radius: {CONTAINER_BORDER_RADIUS}px;
        }}

        QLabel {{
            color: {TEXT_COLOR};
            background: {TRANSPARENT};
            border: none;
        }}

        QPushButton {{
            background: {COLORS[kind]};
            color: {TEXT_COLOR};
            border: none;
            border-radius: {BUTTON_BORDER_RADIUS}px;
            padding: {BUTTON_PADDING};
        }}

        QPushButton:hover {{
            background: {hover_background};
        }}
    """


def transparent_frame_style():
    return f"""
        QFrame {{
            background: {TRANSPARENT};
            border: none;
        }}
    """


def bold_label_style():
    return f"font-weight: {FONT_WEIGHT_BOLD};"

def container_title_style():
    return f"""
        QLabel {{
            font-size: {FONT_SIZE}px;
            font-weight: bold;
            color: {TEXT_COLOR};
            background: transparent;
            border: none;
        }}
    """


def container_count_style():
    return f"""
        QLabel {{
            font-size: {CONTAINER_COUNT_FONT_SIZE}px;
            color: {TEXT_COLOR};
            background: transparent;
            border: none;
        }}
    """

