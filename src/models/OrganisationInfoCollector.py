from src import utils
from bs4 import BeautifulSoup


class OrganisationInfoCollector:
    def __init__(self, url):
        self._url = url if 'http://zakupki.gov.ru' in url else 'http://zakupki.gov.ru' + url

    def run(self):
        html_code = utils.get_html_resp(self._url)
        clear_html_code = BeautifulSoup(html_code, "html5lib")
        title = clear_html_code.head.title.getText()
        notice_tabs = clear_html_code.find("div", {"class": "noticeTabBox"}).findAll("div")
        if title == "Сведения закупки":
            self.get_data_from_purchase_info(notice_tabs[1])
        elif title == "":
            self.get_data_from_general_info(notice_tabs[1].findAll("tr"), notice_tabs[2])

    def get_data_from_purchase_info(self, purchase_info):
        result_dict = {}
        organisation_info = purchase_info.findAll("tbody")[0].findAll("tr")
        result_dict["name"] = organisation_info[0].findAll("td")[1].getText() if not \
            organisation_info[0].findAll("td")[1].a else organisation_info[0].findAll("td")[1].a.getText()
        for item in organisation_info:
            if "Ответственное должностное лицо" in item.findAll("td")[0].getText():
                result_dict["person"] = item.findAll("td")[1].getText()
            elif "Адрес электронной почты" in item.findAll("td")[0].getText():
                result_dict["email"] = item.findAll("td")[1].getText()
        print(result_dict)

    def get_data_from_general_info(self, organisation_info, person_info):
        result_dict = {}
        result_dict["name"] = organisation_info[0].findAll("td")[1].getText() if not \
            organisation_info[0].findAll("td")[1].a else organisation_info[0].findAll("td")[1].a.getText()
        print(result_dict)
