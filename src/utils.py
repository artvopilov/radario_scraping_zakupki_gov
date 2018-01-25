import requests


def get_html_resp(url):
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    if response.status_code != 200:
        raise Exception("Status code: {} URL: {}".format(response.status_code, url))
    html_code = response.text
    return html_code
