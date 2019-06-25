
from bs4 import BeautifulSoup
from connect import *



class Parsing:
    def getHotLink(self):
        html_doc = driver.page_source
        soup = BeautifulSoup(html_doc, 'html.parser')
        hotlink = []
        for link in soup.find_all('a'):
            try:
                if link.get('href').find('restaurants') != -1:
                    if link.get('href').find('restaurant_key') == -1:
                        hotlink.append(link.get('href'))
            except AttributeError:
                continue
        return list(set(hotlink))

    def parsingHot(self, url):
        connect(url)
        html_doc = driver.page_source
        soup = BeautifulSoup(html_doc, 'html.parser')

        try:
            title = soup.find("h1", {"class": "restaurant_name"})
            rating = soup.find("strong", {"class": "rate-point"})
            info = dict()
            info['이름'] = title.get_text()
            info['평점'] = rating.get_text().replace('\n', ' ')
            table = soup.find("tbody")
            for thtd in table.find_all("tr"):
                if thtd.th.get_text() != "메뉴":
                    temp = thtd.th.get_text().replace(' ', '')
                    info[temp.replace('\n', '')] = thtd.td.get_text().replace(
                        '\n', '')
                else:
                    info[thtd.th.get_text()] = thtd.td.get_text()

            return info
        except AttributeError:
            pass
