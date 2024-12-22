import dotenv
import os

dotenv.load_dotenv()

required_vars = [
    'REDDIT_CLIENT_ID', 
    'REDDIT_CLIENT_SECRET', 
    'REDDIT_APP_NAME', 
    'OPENAI_API_KEY', 
    'ALPHA_VANTAGE_API_KEY', 
    "NEWS_API_KEY"
]
env = {}

for var in required_vars:
    value = os.environ.get(var)
    if not value:
        raise ValueError(f"Environment variable {var} is not set")
    env[var] = value