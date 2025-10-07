import os
import sys
import urllib.request
import datetime
import time
import json
import urllib.parse

client_id = '1LMzKQS_OrlkK28JHXTD'
client_secret = 'ary91bS_14'

def getRequestUrl(url):
  req = urllib.request.Request(url)
  req.add_header("X-Naver-Client-Id", client_id)
  req.add_header("X-Naver-Client-Secret", client_secret)

  try:
    response = urllib.request.urlopen(req)
    if response.getcode() == 200:
      print("[%s] Url Request Success" % datetime.datetime.now())
      return response.read().decode('utf-8')
  except Exception as e:
    print(e)
    print("[%s] Error for URL: %s" % (datetime.datetime.now(),url))
    return None
  
def getNaverSearch(node, srcText, start, display):
  base = 'https://openapi.naver.com/v1/search' # 네이버 검색 API
  node = "/%s.json" % node 
  parameters = "?query=%s&start=%s&display=%s" % (urllib.parse.quote(srcText), start, display)

  url = base + node + parameters
  responseDecode = getRequestUrl(url)

  if(responseDecode == None):
    return None
  else:
    return json.loads(responseDecode) # 요청 결과 json으로 받기
  
def getPostData(post, jsonResult, cnt):
  title = post['title']
  description = post['description']
  bloggerlink = post['bloggerlink']
  link = post['link']

  # 블로그 포스트 날짜 형식 수정
  pDate = datetime.datetime.strptime(post['postdate'], '%Y%m%d')
  pDate = pDate.strftime('%Y-%m-%d')

  jsonResult.append({
    'cnt':cnt, 
    'title':title, 
    'description':description,
    'bloggerlink':bloggerlink, 
    'link':link, 
    'postdate':pDate
  })

  return 

def main(): #[CODE 0]
  node = 'blog' #크롤링할 대상
  srcText = input('검색어를 입력하세요: ') # 검색어 지정
  cnt = 0 # 검색 결과 카운트
  jsonResult = [] # 검색 결과를 정리하여 저장할 리스트 객체

  jsonResponse = getNaverSearch(node, srcText, 1, 100) #[CODE 2]
  total = jsonResponse['total']

  while ((jsonResponse != None) and (jsonResponse['display'] != 0)): # 응답받은 데이터가 null이 아니거나 데이터가 0이 될 때까지 반복
    for post in jsonResponse['items']:
      cnt += 1
      getPostData(post, jsonResult, cnt) #[CODE 3]

    start = jsonResponse['start'] + jsonResponse['display']
    if start == 1001:break # 네이버 뉴스는 1000개 까지만 무료로 제공 됨
    jsonResponse = getNaverSearch(node, srcText, start, 100) #[CODE 2]

  print('전체 검색 : %d 건' %total)

  with open('%s_naver_%s.json' % (srcText, node), 'w', encoding = 'utf8') as outfile:
    jsonFile = json.dumps(jsonResult, indent = 4, sort_keys = True, ensure_ascii = False)
    outfile.write(jsonFile)

  print("가져온 데이터 : %d 건" %(cnt))
  print('%s_naver_%s.json SAVED' % (srcText, node))

if __name__ == "__main__":
    main()