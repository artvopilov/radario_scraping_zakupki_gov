import requests
import time


def get_html_resp(url):
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    while response.status_code != 200:
        print("status_code: {}".format(response.status_code))
        time.sleep(1)
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    html_code = response.text
    return html_code
