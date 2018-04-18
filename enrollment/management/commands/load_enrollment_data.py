from csv import DictReader
from datetime import datetime
import pandas as pd 

from django.core.management import BaseCommand

from enrollment.models import EnrollmentItemByYear
from .helpers import get_unemployment_data
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
    if EnrollmentItemByYear.objects.exists():
      print('Enrollment data already loaded... existing.')
      print(ALREADY_LOADED_ERROR_MESSAGE)
      return
    print('-'*30)
    print('Creating enrollment data')
    
    enrollment_df = pd.read_csv('./enrollment_data.csv')

    # if in production mode get the latest unemployment data
    if !DEBUG:
      get_unemployment_data()

    unemployment_df = pd.read_csv('./unemployment_data.csv')
    df = pd.merge(enrollment_df, unemployment_df, how='inner', on=['year'])

    for _, row in df.iterrows():
      enrollmentItemByYear = EnrollmentItemByYear()
      enrollmentItemByYear.year = row['year']
      enrollmentItemByYear.isFall = row['isFall']
      enrollmentItemByYear.enrollment = row['enrollment']
      enrollmentItemByYear.attemptedCredits = row['attemptedCredits']
      enrollmentItemByYear.contactHours = row['contactHours']
      enrollmentItemByYear.unemploymentRateLastYear = row['unemploymentRateLastYear']
      enrollmentItemByYear.save()
    print('Enrollment data loaded.')
    print('-'*30)
    