import urllib.request
import datetime
import time
import json
import pandas as pd

ServiceKey = '0VGmzq6hyxxRhjYc0ZS1Fq2tHHoBnbBYMKCMbDKtnebtUS44dvI%2B0GuldwLIW3nk7d4rqcxFsPss9Fm6RQlWRQ%3D%3D'

def getRequestUrl(url):
  req = urllib.request.Request(url)

  try:
    response = urllib.request.Request(url)
    if response.getcode() == 200:
      print("[%s] Url Request Success" % datetime.datetime.now())
      return response.read().decode('utf-8')
  except Exception as e:
    print(e)
    print("[%s] Error for Url : %s" % datetime.datetime.now(), url)
    return None

def getTourismStatsItem(yyyymm, national_code, ed_cd):
  service_url = "http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList"

  parameters = "?_type=json&servicekey=" + ServiceKey
  parameters += "&YM=" + yyyymm
  parameters += "&NAT_CD=" + national_code
  parameters += "&ED_CD=" + ed_cd

  url = service_url + parameters
  print(url) # 엑세스 거부 여부 확인용 출력
  responseDecode = getRequestUrl(url)

  if(responseDecode == None):
    return None
  else:
    return json.loads(responseDecode)
  
def getTourismStatsService(nat_cd, ed_cd, nStartYear, nEndYear):
  jsonResult = []
  result = []
  natName = ''
  dataEND = "{0}{1:0>2}".format(str(nEndYear), str(12))
  isDataEnd = 0 #데이터 끝 확인용 flag 초기화
  for year in range(nStartYear, nEndYear+1):
    for month in range(1,13):
      if(isDataEnd == 1): break #수집기간이 남았어도 데이터 끝이면 작업 중지
      yyyymm = "{0}{1:0>2}".format(str(year), str(month))
      jsonData = getTourismStatsItem(yyyymm, nat_cd, ed_cd)
      if(jsonData['response']['header']['resultMsg'] == 'OK'):
        if jsonData['response']['body']['items'] == '' : # 데이터가 없는 마지막 항목인 경우
          isDataEnd = 1
          if(month-1) == 0: # 마지막 데이터가 12월인데, 현재 month가 다음해 1월인 경우, year와 month 변수 값 조정
            Year = year - 1
            month - 13
          dataEND = "{0}{1:0>2}".format(str(year), str(month-1))
          print("데이터 없음....\n제공되는 통계 데이터는 $s년 %s월까지 입니다." %(str(year), str(month-1)))
          jsonData = getTourismStatsItem(dataEND, nat_cd, ed_cd) # 출력용으로 마지막 데이터 다시 호출
          break
        natName = jsonData['response']['body']['items']['item' ]['natKorNm’']
        natName = natName.replace(' ', '')
        num = jsonData['response']['body']['items']['item']['num']
        ed = jsonData['response']['body']['items']['item']['ed']
        print('[ %s_%s : %s ]' %(natName, yyyymm, num))

  
def main():
  jsonResult = []
  result = []
  natName = ''

  print("<< 국내 입국한 외국인의 통계 데이터를 수집합니다. >>")
  nat_cd = input('국가 코드를 입력하세요(중국:112 / 일본:130 / 미국:275) : ')
  nStartYear = int(input('데이터를 몇 년부터 수집할까요? : '))
  nEndYear = int(input('데이터를 몇 년까지 수집할까요? : '))
  ed_cd = "E" # E: 방한외래관광객, D: 해외 출국

  jsonResult, result, natName, ed, dataEND = getTourismStatsService(nat_cd, ed_cd, nStartYear, nEndYear)

  if(natName == ''): # 요청은 성공하였지만, 데이터 제공이 안된 경우
    print('데이터가 전달되지 않았습니다. 공공데이터 포탈 서비스 상태를 확인하기 바랍니다.')
  else:
    # 파일 저장1 : json파일
    with open('./%s_%s_%d_%s.json' % (natName, ed, nStartYear, dataEND), 'w', encoding='utf8') as outfile:
      jsonFile = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
      outfile.write(jsonFile)
    
    # 파일 저장2 : csv파일
    columns = ['입국자국가', '국가코드', '입국연월', '입국자 수']
    result_df = pd.DataFrame(result, columns=columns)
    result_df.to_csv('./%s_%s_%d_%s.csv' % (natName, ed, nStartYear, dataEND), index=False, encoding='cp949')

if __name__ == '__main__':
  main()