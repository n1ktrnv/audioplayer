from pathlib import Path

from fastapi.templating import Jinja2Templates

RESOURCES_DIR = Path('app/resources')
TEMPLATES_DIR = RESOURCES_DIR / 'templates'
AUDIOS_DIR = RESOURCES_DIR / 'audios'

TEMPLATES = Jinja2Templates(directory=TEMPLATES_DIR)

CHUNK_SIZE = 1024 * 1024
