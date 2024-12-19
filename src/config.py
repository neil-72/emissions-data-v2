import os
from dotenv import load_dotenv

load_dotenv()

CLAUDE_API_KEY = os.getenv('CLAUDE_API_KEY')
BRAVE_API_KEY = os.getenv('BRAVE_API_KEY')

SEARCH_YEARS = range(2024, 2020, -1)
MAX_RESULTS_PER_SEARCH = 10
MAX_PDF_SIZE = 50 * 1024 * 1024  # 50MB
DEFAULT_OUTPUT_DIR = 'output'
