import os
from dotenv import load_dotenv

def load_environment(env_name="preprod"):
    env_file = f"configs/{env_name}.env"
    if os.path.exists(env_file):
        load_dotenv(env_file)
    else:
        raise FileNotFoundError(f"Environment file {env_file} not found.")

def get_base_url():
    return os.getenv("BASE_URL")
