from utils.env_loader import load_environment, get_base_url

def test_homepage_title(page):
    load_environment("preprod")
    page.goto(get_base_url())
    assert "Polyester" in page.title()
