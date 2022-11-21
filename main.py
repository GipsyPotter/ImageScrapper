from urllib.request import urlopen
from bs4 import BeautifulSoup

htmldata = urlopen('https://www.nettruyenin.com/truyen-tranh/otonari-no-tenshi-sama-ni-itsunomanika-dame-ningen-ni-sareteita-ken/chap-9.1/923990')
soup = BeautifulSoup(htmldata, 'html.parser')
images = soup.find_all('img')

for item in images:
    print(item['src'])