from amazonstoreprice.exception import UrlNotAmazon, PageNotFound, StoreTemporaryUnavailable, RequestGenericError
from bs4 import BeautifulSoup
import requests


class AmazonStorePrice:

    def normalizeurl(self, url):
        """
        clean the url from referal and other stuff

        :param url(string): amazon url

        :return: string(url cleaned)

        """
        if "://www.amazon" in url:
            return url.split("/ref=")[0]
        else:
            raise UrlNotAmazon("Please check the url, it doesn't contain www.amazon*")

    def normalizeprice(self, price):
        """
        remove the currenty from price

        :param price(string): price tag find on amazon store

        :return: float(price cleaned)

        """
        listreplace = ["EUR ", "$", "£"]
        for replacestring in listreplace:
            price = price.replace(replacestring, "")
        return float(price.replace(",", "."))

    def getpage(self, url, retry_ontemp=False):
        """
        Get the page and raise if status_code is not equal to 200

        :param url(string): normalized(url)

        :param retry_ontemp(bool): if true, retry on 503 error

        :return: bs4(html)
        """
        url = self.normalizeurl(url)
        req = requests.get(url)
        if req.status_code == 200:
            return BeautifulSoup(req.text, "html.parser")
        elif req.status_code == 404:
            raise PageNotFound("Page not found, please check url" % req.status_code)
        elif req.status_code == 503:
            if retry_ontemp:
                return self.getpage(url, retry_ontemp=retry_ontemp)
            else:
                raise StoreTemporaryUnavailable(
                    "The Store return 503 code, Service temporarily unavailable, please retry")
        else:
            raise RequestGenericError("Return Code: %s, please check url" % req.status_code)

    def getprice(self, url, retry_ontemp=False):
        """
        Find the price on AmazonStore starting from URL

        :param url(string): url

        :param retry_ontemp(bool): if true, retry on 503 error

        :return: float(price cleaned)
        """
        body_content = self.getpage(self.normalizeurl(url), retry_ontemp=retry_ontemp)
        return self.normalizeprice(body_content.find("span", {"class": "a-color-price"}).contents[0])
