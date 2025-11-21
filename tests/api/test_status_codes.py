import pytest
import requests
from utils.env_loader import load_environment, get_base_url

@pytest.mark.api
def test_status_code_is_200():
    load_environment("preprod")
    response = requests.get(get_base_url())
    assert response.status_code == 200

