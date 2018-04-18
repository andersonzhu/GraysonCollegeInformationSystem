import requests
import json
from datetime import datetime
import pandas as pd


def get_unemployment_data():

  print('Pulling data from Bureau of Labor Statistics...')
  now = datetime.now()
  headers = {'Content-type': 'application/json'}
  data = json.dumps({"seriesid": ['LNS14000000'], "startyear": "2000", "endyear": str(now.year), 'registrationkey': "592c2213b19343599a3401ca50f2d6d2"})
  p = requests.post('https://api.bls.gov/publicAPI/v2/timeseries/data/', data=data, headers=headers)
  json_data = json.loads(p.text)

  year = []
  rate = []
  for series in json_data["Results"]["series"]:
    for item in series['data']:
        year.append(int(item['year']))
        rate.append(float(item['value']))

  df = pd.DataFrame({'year': year,
                    'rate': rate})

  output = df.groupby(year).mean().rename(index=None, columns={'rate': 'unemployment_rate_last_year'})
  output.to_csv('unemployment_data.csv', index=False)

  print('Unemployment data has been updated!')

