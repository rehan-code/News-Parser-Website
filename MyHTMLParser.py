import urllib.request
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.data = ''
        self.inLI = False
        self.num = 0
        self.limit = 3
        self.url = ''

    def feed(self, data, url):
        self.url = url
        super().feed(data)

    def handle_starttag(self, tag, attrs):
         if tag == 'li' and self.inLI == True:
            self.num = self.num + 1

         if self.num == self.limit:
            return
         if tag == 'li':
            self.inLI = True
            self.data = self.data + '<'+tag+'>'
         elif self.inLI:
            self.data = self.data + '<'+tag
            for name,value in attrs:
               if not value.startswith('http'):
                  # print(self.url + value)
                  self.data = self.data + ' ' +name +'="' + self.url + value + '" '
               self.data = self.data + ' ' +name +'="' + value + '" '
            self.data = self.data + '>'

    def handle_endtag(self, tag):
         if self.num == self.limit:
            return
         if tag == 'li':
            self.inLI = False
            self.num = self.num + 1
            self.data = self.data + '</'+tag+'>'
         elif self.inLI:
            self.data = self.data + '</'+tag+'>'

    def handle_data(self, data):
         if self.num == self.limit:
            return
         if self.inLI:
            self.data = self.data + data
        # print("Encountered some data  :", data)

    def setLimit(self, limit):
         self.limit = limit

    def clearData(self):
         self.data = ''
         self.num = 0