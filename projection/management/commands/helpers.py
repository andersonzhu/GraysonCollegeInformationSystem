import requests
import json
from datetime import datetime
import pandas as pd
import numpy as np 


def get_unemployment_data():
  """
  Use BLS api to pull latest unemployment rate data.
  """

  print('Pulling data from Bureau of Labor Statistics...')
  now = datetime.now()
  headers = {'Content-type': 'application/json'}
  data = json.dumps({"seriesid": ['LNS14000000'], 
                     "startyear": "2000", 
                     "endyear": str(now.year), 
                     "registrationkey": "592c2213b19343599a3401ca50f2d6d2"})
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


def create_test_data(train):
  """
  Create test data based on train data.
  If the last term of train data is Fall semester, 
  it will generate Spring and Fall of next year. 
  Otherwise, it will generate Fall of current year, 
  Spring and Fall for next year.  
  """

  year_col = train['year'].values
  isFall_col = train['isFall'].values
  mx_year = np.max(year_col)
  if isFall_col[-1] == 1:
    year = [mx_year + 1 for x in range(2)]
    isFall = [0, 1]
  else:
    year = [mx_year, mx_year + 1, mx_year + 1]
    isFall = [1, 0, 1]

  test = pd.DataFrame({'year': year, 'isFall': isFall})
  # test['numberOfStudentsPred'] = 0
  # test['attemptedCreditsPred'] = 0
  # test['contactHoursPred'] = 0
  return test 