import requests
from bs4 import BeautifulSoup


year = input("Enter year: ")
rating = input("Enter minimum rating: ")

url = "https://www.imdb.com/search/title/"
data = {
    "title_type": "feature",
    "release_date": year + "-01-01," + year + "-12-31",
    "user_rating": rating + ",",
    "sort": "boxoffice_gross_us,desc"
}
headers = {
    "accept-language": "en"
}
response = requests.get(url, data, headers=headers)
html = response.text

soup = BeautifulSoup(html, features="html.parser")


films = soup.find_all("div", class_="lister-item mode-advanced")
for film in films:
    film_header = film.find("h3", class_="lister-item-header")
    film_title = film_header.a.text

    film_stats = film.find("p", class_="sort-num_votes-visible")
    stats = film_stats.find_all("span", attrs={ "name": "nv" })
    votes = stats[0].text
    if len(stats) == 2:
        gross = stats[1].text
    else:
        gross = "-"

    ratings = film.find("div", class_="ratings-bar")
    film_rating = float(ratings.strong.text)

    # print(film_title)
    # print(film_rating)
    # print(gross)

    print(f"{film_title:<30}{film_rating:<5}{gross}")
    
































# header_index = html.index("lister-item-header")
# a_index = html.index("<a ", header_index)
# title_index = html.index(">", a_index) + 1
# title_end_index = html.index("</", title_index)

# title = html[title_index : title_end_index]


# div_index = html.index("inline-block ratings-imdb-rating")
# strong_index = html.index("strong", div_index)

# rating_index = strong_index + 7
# rating = html[rating_index : rating_index + 3]

# print(title)
# print(rating)