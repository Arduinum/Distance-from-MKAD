from pathlib import Path
from os import environ


BASE_DIR = Path(__file__).resolve().parent
env_path = BASE_DIR / '.env'

# если env_path существует установит переменные среды в environ
if env_path.exists():
    with open(env_path, encoding="utf-8") as file:
        for line in file:
            if not line.strip() or line.strip().startswith('#'):
                continue
            name, value = line.strip().split('=', 1)
            environ[name] = value


API_KEY = environ.get('API_KEY')
