"""
    Example Sitemap extracting script
    requires `requests` http://docs.python-requests.org/en/master/
    & `BeautifulSoup` https://pypi.python.org/pypi/beautifulsoup4
"""
import requests
from bs4 import BeautifulSoup

"""
    Request Sitemap from Deadline.com
"""
RESP = requests.get("http://deadline.com/news-sitemap.xml")
"""
    Parse repsonse.text with BeautifulSoup
    Examples for bs4 here:
    http://web.stanford.edu/~zlotnick/TextAsData/Web_Scraping_with_Beautiful_Soup.html
"""
DEADLINE_SITEMAP = BeautifulSoup(RESP.text)
"""
    Create a List to accumulate results
"""
RESULTS = []

"""
    For each `url` in sitemap extract desired content
    Below is a mapping to NewsCart valid keynames
    loc : (url)
    news:publication_date : (publishedAt)
    news:title : (title)
    image:loc : (urlToImage)
"""
for entry in DEADLINE_SITEMAP.find_all("url"):
    article = {} #Creat Dict to group content
    article["url"] = entry.find("loc").text
    article["publishedAt"] = entry.find("news:publication_date")
    article["title"] = entry.find("news:title").text
    article["urlToImage"] = entry.find("image:loc").text
    RESULTS.append(article)

"""
    Here is where we would probably clean the data(remove old articles)
    or persist to Firebase
"""
print(RESULTS)
