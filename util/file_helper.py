# 기본 entity 파일.
from dataclasses import dataclass
import pandas as pd
import xlrd
import googlemaps
import json

# Path 는 바뀜
"""
context = "/Users/seung/SbaProjects/beatCamp-python"
fname = "/titanic/data"
"""


@dataclass
class FileReader:
    context: str = ''
    fname: str = ''
    train: object = None
    test: object = None
    id: str = ''
    label: str = ''

    def new_file(self) -> str:
        return self.context + self.fname

    def csv_to_df(self) -> object:
        file = self.new_file()
        return pd.read_csv(file, encoding='UTF-8', thousands=',')

    def xls_to_df(self, header, usecols) -> object:
        file = self.new_file()
        return pd.read_excel(file, header = header, usecols = usecols)

    def json_load(self) -> object:
        # 안에 있는 method 까지 쓸거면 dframe. ex DataFrame.head() 등등 
        # 이건 load 만 써서 화면만 볼꺼기 때문에 
        # json_to_df 는 틀린 표현이다.
        file = self.new_file()
        return json.load(open(file, encoding='UTF-8'))

    def create_gmaps(self):
        return googlemaps.Client(key = 'AIzaSyBz9GRH0blpoiLp1co3O5V3hXgwT928jyY')

