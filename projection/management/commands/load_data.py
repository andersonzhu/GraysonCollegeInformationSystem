from csv import DictReader
from datetime import datetime
import pandas as pd 
from sklearn.linear_model import LinearRegression

from django.core.management import BaseCommand

from projection.models import ProjectionItemByYear
from .helpers import get_unemployment_data, create_test_data
from GraysonCollegeInformationSystem.settings import DEBUG

DATETIME_FORMAT = '%m%d%Y'

ALREADY_LOADED_ERROR_MESSAGE = """
If you need to reload the enrollment data from the csv file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty database with tables.
"""


class Command(BaseCommand):
  help = "Loads data from enrollment_data.csv and unemployment_data.csv into our model"

  def handle(self, *args, **options):
    if ProjectionItemByYear.objects.exists():
      print('Enrollment data already loaded... existing.')
      print(ALREADY_LOADED_ERROR_MESSAGE)
      return
    print('-'*30)
    print('Creating enrollment data')
    
    enrollment_df = pd.read_csv('./enrollment_data.csv')

    # if in production mode get the latest unemployment data
    if not DEBUG:
      get_unemployment_data()

    unemployment_df = pd.read_csv('./unemployment_data.csv')
    df_train = pd.merge(enrollment_df, unemployment_df, how='inner', on=['year'])

    # pick years for training???

    # prepare testing data, including year and isFall column
    _test = create_test_data(df_train)
    df_test = pd.merge(_test, unemployment_df, how='inner', on=['year'])
    df_test = pd.concat([df_train[['year', 'isFall', 'unemploymentRateLastYear']], df_test])
    X_test = df_test[['year', 'isFall', 'unemploymentRateLastYear']].values


    # prepare data for model training
    X = df_train[['year', 'isFall', 'unemploymentRateLastYear']].values
    targets = ['numberOfStudents', 'attemptedCredits', 'contactHours']

    for target in targets:
      y = df_train[[target]].values

      lr = LinearRegression()
      lr.fit(X, y)
      df_test[target + 'Pred'] = lr.predict(X_test)

    # merge train and test as df

    for _, row in df_train.iterrows():
      item = ProjectionItemByYear()
      item.year = row['year']
      item.isFall = row['isFall']
      item.semester = item.semesterFullName()
      item.numberOfStudents = row['numberOfStudents']
      item.attemptedCredits = row['attemptedCredits']
      item.contactHours = row['contactHours']
      item.unemploymentRateLastYear = row['unemploymentRateLastYear']
      item.save()
    print('Enrollment data loaded.')
    print('-'*30)
    