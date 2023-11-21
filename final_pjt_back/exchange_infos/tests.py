from django.test import TestCase

# Create your tests here.
from datetime import datetime, timedelta
yesterday = (datetime.today() - timedelta(1)).strftime("%Y%m%d")
print(yesterday)