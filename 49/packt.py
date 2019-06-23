from collections import namedtuple

from bs4 import BeautifulSoup as Soup
import requests

CONTENT = requests.get("http://bit.ly/2EN2Ntv").text

Book = namedtuple("Book", "title description image link")


def get_book():
    """make a Soup object, parse the relevant html sections, and return a Book namedtuple"""

    soup = Soup(CONTENT, "html.parser")

    desc_section = soup.find("div", class_="dotd-main-book-summary float-left")
    img_section = soup.find("div", class_="dotd-main-book-image float-left")

    title = soup.h2.text.strip()
    description = desc_section.find_all("div")[2].text.strip()
    image = img_section.img["src"]
    link = img_section.a["href"]

    free_book = Book(title, description, image, link)

    return free_book
