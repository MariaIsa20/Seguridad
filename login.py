import urllib.parse
import urllib.request

url = 'http://www.wechall.net'
values = {'Username' : 'user',
          'Password' : 'pass'}

data = urllib.parse.urlencode(values)
data = data.encode('ascii') # data should be bytes
#req = urllib.request.Request(url, data)
urllib.request.urlopen(url,data=data)