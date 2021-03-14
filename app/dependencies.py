from pathlib import Path

from dotenv import load_dotenv

dotfile = Path(__file__).resolve().parents[1] / '.env'


def load_env_variables():
    load_dotenv(dotfile)