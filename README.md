BBC News Headlines Scraper
This is a simple Python script that fetches and displays the top 10 headlines from BBC News using the requests and BeautifulSoup libraries.
Features
Scrapes the BBC News homepage (https://www.bbc.com/news)
Extracts the latest headlines from the site
Prints the top 10 headlines in a clean, numbered list
Handles request errors gracefully with proper exception handling
Uses a custom User-Agent to avoid request blocking
Requirements
Make sure you have Python 3 installed.
Install dependencies using pip:
Bash
pip install requests beautifulsoup4
Usage
Run the script directly
Bash
python bbc_headlines.py
Example output:
BBC News Headlines:

1. Headline one
2. Headline two
3. Headline three
...
10. Headline ten
Code Overview
requests → Fetches the BBC News HTML content
BeautifulSoup → Parses the HTML and extracts <h3> tags with class gs-c-promo-heading__title
Loop → Prints the first 10 headlines in a formatted list
Notes
The BBC website structure may change, which could break the scraper. If headlines don’t appear, you may need to inspect the page and update the CSS selector.
Some headlines may be loaded dynamically with JavaScript. This script only works with static HTML. For full scraping, tools like Selenium or Playwright may be required.
License
This project is for educational purposes only. Please respect the BBC Terms of Use.
