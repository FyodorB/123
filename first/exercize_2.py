import requests
from bs4 import BeautifulSoup

url = "https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"
page = requests.get(url).text

while True:
    soup = BeautifulSoup(page, 'lxml')
    animal_category = soup.find("div", class_="mw-category mw-category-columns")
    category_letter = animal_category.find("div", class_="mw-category-group")
    choice_letter = category_letter.find_next("h3").text
    animal_names = animal_category.find_all("li")

    lst_animal =[]
    dict_animal = {}
    dict_animal_res = {}
    value_animal = 0
    for name in animal_names:
        lst_animal.append(name.text)
    for animal in lst_animal:
        if animal.startswith(choice_letter):
            value_animal += 1
    dict_animal.update(({choice_letter: value_animal}))
    for key, value in dict_animal.items():
        print(f"{key}: {value}")

    links = soup.find('div', id='mw-pages').find_all('a')
    for a in links:
        if a.text == 'Следующая страница':
            url = 'https://ru.wikipedia.org/' + a.get('href')
            page = requests.get(url).text







