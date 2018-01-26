from src import utils
from bs4 import BeautifulSoup


class LinkCollector:
    def __init__(self, url):
        self._url = url

    def run(self):
        html_code = utils.get_html_resp(self._url)
        clear_html_code = BeautifulSoup(html_code, "html5lib")
        theatre_cards = clear_html_code.html.body.findAll("div", {"class": "registerBox"})
        cards_links = list(card.find("td", {"class": "descriptTenderTd"}).a["href"] for card in theatre_cards)
        return cards_links
