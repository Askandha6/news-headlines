import requests
from bs4 import BeautifulSoup

# Choose your target news website URL
url = "https://lite.cnn.com/"

# Fetch the web page
response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
soup = BeautifulSoup(response.text, "html.parser")

# Find all headline elements (update selector as per site)
headlines = soup.find_all(class_="card--lite")

# Print the headlines
for headline in headlines:
    print(headline.get_text())
