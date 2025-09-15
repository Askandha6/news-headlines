# news-headlines
import requests
from bs4 import BeautifulSoup

url = "https://lite.cnn.com/"

response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
soup = BeautifulSoup(response.text, "html.parser")

headlines = soup.find_all(class_="card--lite")

for headline in headlines:
    print(headline.get_text())
