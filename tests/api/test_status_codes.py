import requests
from utils.env_loader import load_environment, get_base_url

def test_homepage_status_code():
    load_environment("preprod")
    response = requests.get(get_base_url())
    assert response.status_code == 200
