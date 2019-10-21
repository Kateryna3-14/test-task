import sys
from bs4 import BeautifulSoup
import urllib
from urllib import request

basic_url = sys.argv[1]
diff_url = sys.argv[2]


class ButtonFinder:
    def __init__(self, basic_url, diff_url):
        self.basic_url = basic_url
        self.diff_url = diff_url

    def basic(self, url):
        response = urllib.request.urlopen(url)
        text_from_response = response.read().decode('utf-8')
        response_xml_format = BeautifulSoup(text_from_response, 'xml')
        return response_xml_format

    def get_needed_attributes(self):
        soup = self.basic(self.basic_url)
        needed_attrs = soup.find_all(attrs={'id': 'make-everything-ok-button'})[0].attrs
        del needed_attrs['id']
        list_needed_attrs = list(needed_attrs.keys())
        return list_needed_attrs

    def find_needed_button(self):
        response_xml_format = self.basic(self.diff_url)
        needed_attrs = self.get_needed_attributes()
        needed_elements_without_filter = response_xml_format.find_all('a')
        for i in needed_elements_without_filter:
            if all(k in i.attrs for k in tuple(needed_attrs)):
                return i


needed_button = ButtonFinder(basic_url,diff_url).find_needed_button()
print(needed_button)
