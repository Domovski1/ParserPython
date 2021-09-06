# pip install beautifulsoup4, lxml
from bs4 import BeautifulSoup


with open("blank/index.html") as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")

# Получаем имя юзера
user_name = soup.find("div", class_="user__name").find("span").text


find_all_spans_in_user_info = soup.find(class_="user__info").find_all("span")

# for item in find_all_spans_in_user_info:
#     print("[INFO]", item.text)

social_link = soup.find(class_="social__networks").find("ul").find_all("a")

for item in social_link:
    item_text = item.text
    item_url = item.get("href")
    print(f"{item_text}: {item_url}")