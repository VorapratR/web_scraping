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


def get_number(values):
    try:
        result = 0
        for value in values:
            if is_float(value) == True:
                result = float(value)
        return(result)
    except:
        return 0


def investing_scraping(input):
    try:
        url = f"https://www.investing.com/equities/{input}"
        headers = {"User-Agent": "Mozilla/5.0"}
        res = Request(url, headers=headers)
        web_data = urlopen(res).read()
        soup = BeautifulSoup(web_data, "html.parser")
        head = soup.find("div", {
            "class": "instrument-price_instrument-price__3uw25 instrument-price_instrument-price-lg__3ES-Q flex items-end flex-wrap"})
        first_value = head.find(
            "span", {"class": "instrument-price_last__KQzyA"})
        first_value = get_number(first_value.contents)
        second_value = head.find("span", {
            "class": "instrument-price_change-value__jkuml instrument-price_up__2-OcT"})
        second_value = get_number(second_value.contents)
        third_value = head.find("span", {
            "class": "instrument-price_change-percent__19cas instrument-price_up__2-OcT"})
        third_value = get_number(third_value.contents)
        return [first_value, second_value, third_value]
    except:
        return None
