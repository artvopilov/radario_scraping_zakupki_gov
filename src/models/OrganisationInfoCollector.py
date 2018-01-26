from src import utils
from bs4 import BeautifulSoup


class OrganisationInfoCollector:

    @staticmethod
    def run(self, url):
        url = url if 'http://zakupki.gov.ru' in url else 'http://zakupki.gov.ru' + url
        html_code = utils.get_html_resp(url)
        clear_html_code = BeautifulSoup(html_code, "html5lib")
        title = clear_html_code.head.title.getText()
        notice_tabs = clear_html_code.findAll("div", {"class": "noticeTabBox"})[-1].findAll("div")
        if len(list(notice_tabs)) < 2:
            return False
        if title == "Сведения закупки":
            return self.get_data_from_purchase_info(notice_tabs[1])
        elif title == "Общая информация":
            return self.get_data_from_general_info(notice_tabs[1].findAll("tr"), notice_tabs[2].findAll("tr"))
        elif "Учетная карточка организации":
            return False

    @staticmethod
    def get_data_from_purchase_info(purchase_info):
        result_dict = {}
        organisation_info = purchase_info.findAll("tbody")[0].findAll("tr")
        result_dict["name"] = str(organisation_info[0].findAll("td")[1].getText()) if not \
            organisation_info[0].findAll("td")[1].a else str(organisation_info[0].findAll("td")[1].a.getText())
        for item in organisation_info:
            if "Ответственное должностное лицо" in item.findAll("td")[0].getText():
                result_dict["person"] = str(item.findAll("td")[1].getText().strip())
            elif "Адрес электронной почты" in item.findAll("td")[0].getText():
                result_dict["email"] = str(item.findAll("td")[1].getText().strip())
        print(result_dict)
        return result_dict

    @staticmethod
    def get_data_from_general_info(organisation_info, person_info):
        result_dict = {}
        result_dict["name"] = str(organisation_info[0].findAll("td")[1].getText()) if not \
            organisation_info[0].findAll("td")[1].a else str(organisation_info[0].findAll("td")[1].a.getText())
        for item in person_info:
            if "Контактное лицо" in item.findAll("td")[0].getText():
                result_dict["person"] = str(item.findAll("td")[1].getText().strip())
            elif "Электронная почта" in item.findAll("td")[0].getText():
                result_dict["email"] = str(item.findAll("td")[1].getText().strip())
        print(result_dict)
        return result_dict
