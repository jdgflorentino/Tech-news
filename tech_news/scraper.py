import requests
import time
import parsel
import re
from tech_news.database import create_news


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
    selector = parsel.Selector(html_content)
    list = selector.css(".cs-overlay-link::attr(href)").getall()

    return list


# Requisito 3
def scrape_next_page_link(html_content):
    selector = parsel.Selector(html_content)
    scrape = selector.css(".next::attr(href)").get()
    return scrape


# Requisito 4
def scrape_noticia(html_content):
    selector = parsel.Selector(html_content)

    url = selector.css("link[rel='canonical']::attr(href)").get()

    title = re.sub(r"\s+$", "", selector.css(".entry-title::text").get())

    timestamp = selector.css(".meta-date::text").get()

    writer = selector.css(".fn::text").get()

    comments_count = selector.css(
        ".title-block::text").re_first(r"\d") or 0

    summary = re.sub(r"\s+$", "", selector.xpath("string(//p)").get())

    tags = selector.css(".post-tags li a::text").getall()

    category = selector.css(".category-style span.label::text").get()

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "comments_count": comments_count,
        "summary": summary,
        "tags": tags,
        "category": category,
        }


# Requisito 5
def get_tech_news(amount):
    news = []
    url = "https://blog.betrybe.com/"
    while len(news) < amount:
        page = fetch(url)
        pages = scrape_novidades(page)
        for link in pages:
            if len(news) < amount:
                news.append(scrape_noticia(fetch(link)))
        url = scrape_next_page_link(page)
    create_news(news)
    return news
