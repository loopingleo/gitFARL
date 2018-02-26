import requests
import pandas

url = "https://api.intrinio.com/companies?ticker=AAPL"

data =requests.get(url=url,
                   auth=('b8c35d9fb327b61a6f263165a392494e',
                         'cc3b202a74ea05414a7fe095a1b29bc3'))

data.json()

data.content

data = pd.read_json("https://api.intrinio.com/companies?ticker=AAPL", auth=('b8c35d9fb327b61a6f263165a392494e',
                         'cc3b202a74ea05414a7fe095a1b29bc3'))

from urllib2 import Request, urlopen
import json
from pandas.io.json import json_normalize

path1 = '42.974049,-81.205203|42.974298,-81.195755'
request=requests.get('http://maps.googleapis.com/maps/api/elevation/json?locations='+path1+'&sensor=false')

request.json()

response = urlopen(request)
elevations = response.read()
data = json.loads(elevations)
json_normalize(data['results'])