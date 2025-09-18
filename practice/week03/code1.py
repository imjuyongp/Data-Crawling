def getRequestUrl(url):
  req = urllib.request.Request(url)
  req.add_header("X-Naver-Client-Id", client_id)
  req.add_header("X-Naver-Client-Secret", client_secret)

  try:
    reposnse = urllib.request.urlopen(req)
    if response.getcode() == 200:
      print("[%s] Url Request Success" % datetime.datetime.now())
      return response.read().decode('utf-8')
  except Exception as e:
    print(e)
    print("[%s] Error for URL: %s" % (datetime.datetime.now(),url))
    return None