#!python
#encoding:utf-8

import requests
import json
import urllib
import sys

def Schedule(a,b,c):
  '''
  a:已经下载的数据块
  b:数据块的大小
  c:远程文件的大小
  '''
  per = 100.0 * a * b / c
  if per > 100:
    per = 100
  sys.stdout.write(u'\r已下载%.2f%%' % per)
  sys.stdout.flush()


#title:歌曲名
#choose:0默认自动下载, 否则自己选择
#0下载成功, -1下载失败
def musicDownload(title, choose=0):
  url = 'https://muc.cheshirex.com/'
  params = {
    'input': title,
    'filter': 'name',
    'type': 'qq',#netease,qq,kugou,kuwo,xiami,baidu.1ting,migu,lizhi,qingting,ximalaya,kg
    'page': '1'
  }
  headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
  }
  try:
    html = requests.post(url, params, headers=headers)
    res = json.loads(html.text)
    if choose == 0:
      urllib.urlretrieve(res['data'][0]['url'], res['data'][0]['author'] + ' - ' + res['data'][0]['title']+".mp3", Schedule)
      print ''
      return 0
    else:
      i = 0
      for tmp in res['data']:
        print i,
        print tmp['title']+'      '+tmp['author']
        i = i + 1
      j = input('input the music id:')
      if j >= 0 and j < len(res['data']):
        urllib.urlretrieve(res['data'][j]['url'], res['data'][j]['author'] + ' - ' + res['data'][j]['title']+".mp3")
        print ''
        return 0
      else:
        return -1
  except:
    return -1


if __name__ == "__main__":
  ret = musicDownload('胡广生', 0)
  print ret