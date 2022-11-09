import requests
import time


# Requisito 1
def fetch(url):
    try:
        page = requests.get(url, timeout=3,
                            headers={"user-agent": "Fake user-agent"})
        page.raise_for_status()
        time.sleep(1)
        return page.text

    except BaseException:
        return None


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
