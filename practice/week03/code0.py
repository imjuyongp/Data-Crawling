import json

def main(): #[CODE 0]
  node = 'news' #크롤링할 대상
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
    jsonResponse = getNaverSearch(node, srcText, start, 100) #[CODE 2]

  print('전체 검색 : %d 건' %total)

  with open('%s_naver_%s.json' % (srcText, node), 'w', encoding = 'utf8’) as outfile:
    jsonFile = json.dumps(jsonResult, indent = 4, sort_keys = True, ensure_ascii = False)

    outfile.write(jsonFile)

  print("가져온 데이터 : %d 건" %(cnt))
  print('%s_naver_%s.json SAVED' % (srcText, node))