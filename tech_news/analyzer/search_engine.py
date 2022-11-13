from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    list = search_news({"title": {"$regex": title, "$options": "i"}})
    return [(news["title"], news["url"]) for news in list]


# Requisito 7
def search_by_date(date):
    try:
        date_format = datetime.fromisoformat(date).strftime("%d/%m/%Y")
        list = search_news({"timestamp": {"$regex": date_format}})
    except ValueError:
        raise ValueError("Data inválida")
    return [(news["title"], news["url"]) for news in list]


# Requisito 8
def search_by_tag(tag):
    list = search_news({"tags": {"$regex": tag, "$options": "i"}})
    return [(news["title"], news["url"]) for news in list]


# Requisito 9
def search_by_category(category):
    list = search_news({"category": {"$regex": category, "$options": "i"}})
    return [(news["title"], news["url"]) for news in list]
