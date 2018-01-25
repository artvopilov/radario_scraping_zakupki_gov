from models.LinkCollector import LinkCollector
from models.OrganisationInfoCollector import OrganisationInfoCollector
from settings import settings
from bs4 import BeautifulSoup
from src import utils


def get_pages_num(url):
    html_code = utils.get_html_resp(url)
    clear_html_code = BeautifulSoup(html_code, "html5lib")
    last_page = clear_html_code.find("ul", {"class": "paging"}).findAll("li")[-2].a.getText()
    return last_page


if __name__ == "__main__":
    org_in_col = OrganisationInfoCollector('/epz/order/notice/ep44/view/common-info.html?regNumber=0319300053118000001')
    org_in_col.run()
    # theatre_pages_num = int(get_pages_num(settings["theatreUrl"](1)))
    # museum_pages_num = int(get_pages_num(settings["museumUrl"](1)))
    #
    # theatre_card_links_by_pages = []
    # museum_card_links_by_pages = []
    #
    # for i in range(theatre_pages_num):
    #     mail_collector = LinkCollector(settings["theatreUrl"](i + 1))
    #     theatre_card_links_by_pages.append(mail_collector.run())
    #
    # for i in range(theatre_pages_num):
    #     mail_collector = LinkCollector(settings["museumUrl"](i + 1))
    #     museum_card_links_by_pages.append(mail_collector.run())


