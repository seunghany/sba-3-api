# 기본 entity 파일.
from dataclasses import dataclass
import pandas as pd
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

    