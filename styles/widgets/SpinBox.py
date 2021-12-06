import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from styles.styles import colors

SpinBox = f"""
    QSpinBox {{
        background-color: {colors['background']};
        color: {colors['text']};
        font-size: 16px;
        padding: 5px 8px;
        border-radius: 5px;
    }}
"""