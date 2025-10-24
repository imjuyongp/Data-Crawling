import urllib.request
URL = 'https://www.cheogajip.co.kr/bbs/board.php?bo_table=store&page=1'
response = urllib.request.urlopen(URL)
from bs4 import BeautifulSoup 
soupData = BeautifulSoup(response, 'html.parser')
tbody_tag = soupData.find('tbody')
store_tr = tbody_tag.findAll('tr')
store_tr[0]