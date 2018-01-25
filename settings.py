settings = {
    "theatreUrl": lambda page: "http://www.zakupki.gov.ru/epz/order/quicksearch/"
                               "search_eis.html?searchString="
                               "%D1%82%D0%B5%D0%B0%D1%82%D1%80&pageNumber={}&"
                               "sortDirection=false&recordsPerPage=_10&"
                               "showLotsInfoHidden=false&fz44=on&fz223=on&"
                               "af=on&ca=on&pc=on&pa=on&priceFrom=&priceTo=&"
                               "currencyId=1&agencyTitle=&agencyCode=&"
                               "agencyFz94id=&agencyFz223id=&agencyInn=&"
                               "regions=&publishDateFrom=&publishDateTo=&"
                               "sortBy=UPDATE_DATE&updateDateFrom="
                               "&updateDateTo=".format(page),
    "museumUrl": lambda page: "http://www.zakupki.gov.ru/epz/order/quicksearch/"
                              "search_eis.html?searchString="
                              "%D0%BC%D1%83%D0%B7%D0%B5%D0%B9&pageNumber={}&"
                              "sortDirection=false&recordsPerPage=_10&"
                              "showLotsInfoHidden=false&fz44=on&fz223=on&"
                              "af=on&ca=on&pc=on&pa=on&currencyId=1&"
                              "sortBy=UPDATE_DATE".format(page)
}
