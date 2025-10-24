import urllib.request
URL = 'https://www.cheogajip.co.kr/bbs/board.php?bo_table=store&page=1'
response = urllib.request.urlopen(URL)
from bs4 import BeautifulSoup 
soupData = BeautifulSoup(response, 'html.parser')
tbody_tag = soupData.find('tbody')
store_tr = tbody_tag.findAll('tr')
store_tr[0]

store_tr_str = list(store_tr[0].strings)
store_tr_str
store_tr_str[1]
store_tr_str[3]
store_tr_str[5]
