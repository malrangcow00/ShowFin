import requests, sys
from pprint import pprint
import pandas as pd


def get_response(url):
    response = requests.get(url)
    data = response.json()
    return data


fin_API_KEY = 'f5e5273d3415b407b8b70072028c8174'
deposit_products_API_URL = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={fin_API_KEY}&topFinGrpNo=020000&pageNo=1'
saving_products_API_URL = f'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={fin_API_KEY}&topFinGrpNo=020000&pageNo=1'

sys.stdout = open('deposit_products.txt', 'w')
pprint(get_response(deposit_products_API_URL))
df = pd.read_csv(deposit_products.txt)

sys.stdout = open('saving_products.txt', 'w')
pprint(get_response(saving_products_API_URL))





