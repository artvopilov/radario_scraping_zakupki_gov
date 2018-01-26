from models.LinkCollector import LinkCollector
from models.OrganisationInfoCollector import OrganisationInfoCollector
from settings import settings
from bs4 import BeautifulSoup
from src import utils
import xlsxwriter


def get_pages_num(url):
    html_code = utils.get_html_resp(url)
    clear_html_code = BeautifulSoup(html_code, "html5lib")
    last_page = clear_html_code.find("ul", {"class": "paging"}).findAll("li")[-2].a.getText()
    return last_page


if __name__ == "__main__":
    theatre_pages_num = int(get_pages_num(settings["theatreUrl"](1)))
    museum_pages_num = int(get_pages_num(settings["museumUrl"](1)))

    theatre_card_links_by_pages = []
    museum_card_links_by_pages = []

    for i in range(theatre_pages_num):
        link_collector = LinkCollector(settings["theatreUrl"](i + 1))
        for link in link_collector.run():
            theatre_card_links_by_pages.append(link)

    for i in range(museum_pages_num):
        link_collector = LinkCollector(settings["museumUrl"](i + 1))
        for link in link_collector.run():
            museum_card_links_by_pages.append(link)

    workbook = xlsxwriter.Workbook('..\zakupkiScrapingResult.xlsx')
    worksheet = workbook.add_worksheet()

    worksheet.write('A1', "Театры")
    for i in range(len(theatre_card_links_by_pages)):
        theatre_info = OrganisationInfoCollector.run(OrganisationInfoCollector, theatre_card_links_by_pages[i])
        if not theatre_info:
            print("No Info")
            continue
        try:
            worksheet.write('A{}'.format(i + 2), theatre_info["name"])
            if "person" in theatre_info.keys():
                worksheet.write('B{}'.format(i + 2), theatre_info["person"] if theatre_info["person"] else "none")
            else:
                worksheet.write('B{}'.format(i + 2), "none")
            if "email" in theatre_info.keys():
                worksheet.write('C{}'.format(i + 2), theatre_info["email"] if theatre_info["email"] else "none")
            else:
                worksheet.write('C{}'.format(i + 2), "none")
        except:
            print("EXCEPTION while writing")
            pass

    worksheet.write('A{}'.format(2 + len(theatre_card_links_by_pages)), "Музеи")
    for i in range(len(museum_card_links_by_pages)):
        museum_info = OrganisationInfoCollector.run(OrganisationInfoCollector, museum_card_links_by_pages[i])
        if not museum_info:
            print("No Info")
            continue
        try:
            worksheet.write('A{}'.format(i + 3 + len(theatre_card_links_by_pages)), museum_info["name"])
            if "person" in museum_info.keys():
                worksheet.write('B{}'.format(i + 3 + len(theatre_card_links_by_pages)),
                                museum_info["person"] if museum_info["person"] else "none")
            else:
                worksheet.write('B{}'.format(i + 3 + len(theatre_card_links_by_pages)), "none")
            if "email" in museum_info.keys():
                worksheet.write('C{}'.format(i + 3 + len(theatre_card_links_by_pages)),
                                museum_info["email"] if museum_info["email"] else "none")
            else:
                worksheet.write('C{}'.format(i + 3 + len(theatre_card_links_by_pages)), "none")
        except:
            print("EXCEPTION while writing")
            pass

    workbook.close()
