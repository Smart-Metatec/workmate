import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from widgetStyles.styles import color, mode, default, dark_blue, light_blue
from utils.globals import ASSET_PATH
import assets.resources

DateEdit = f"""
    QDateEdit {{
        border: none;
        color: {default};
        font-size: 12px;
        height: 30px;
    }}
    QDateEdit::drop-down {{
        background-color: {mode};
        border: 2px solid {light_blue};
        color: {default};
        padding: 5px;
        border-radius: 5px;
        width: 40px;

        image: url(:/other/calendar.svg);
    }}
"""