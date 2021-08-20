from bs4 import BeautifulSoup
from urllib.request import Request, urlopen


def ml_model(lst_x=[1, 2, 3, 4, 5]):
    y = (lst_x[-1]+lst_x[-2]+lst_x[-3])/3
    return y


def is_float(value):
    try:
        float(value)
        return True
    except:
        return False


def getNumer(datas):
    result = 0
    for data in datas:
        if is_float(data) == True:
            result = float(data)
    return(result)


def web_scraping(input):
    url = f"https://www.investing.com/equities/{input}"
    headers = {"User-Agent": "Mozilla/5.0"}
    res = Request(url, headers=headers)
    web_data = urlopen(res).read()
    soup = BeautifulSoup(web_data, "html.parser")
    head = soup.find("div", {
        "class": "instrument-price_instrument-price__3uw25 instrument-price_instrument-price-lg__3ES-Q flex items-end flex-wrap"})
    first_value = head.find("span", {"class": "instrument-price_last__KQzyA"})
    first_value = getNumer(first_value.contents)
    second_value = head.find("span", {
        "class": "instrument-price_change-value__jkuml instrument-price_up__2-OcT"})
    second_value = getNumer(second_value.contents)
    third_value = head.find("span", {
        "class": "instrument-price_change-percent__19cas instrument-price_up__2-OcT"})
    third_value = getNumer(third_value.contents)
    return [first_value, second_value, third_value]
