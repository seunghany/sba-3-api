import pandas as pd
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from util.file_handler import FileReader

class Cctv:
    def __init__(self):
        print(f'hello')
        self.reader = FileReader()
    
    def get_cctv(self):
        reader = self.reader
        reader.context = '/Users/seung/SbaProjects/sba-3-api/crime/'
        reader.fname = 'cctv_in_seoul.csv'
        reader.new_file()
        cctv = reader.csv_to_df()
        print(f'{cctv.head()}')

if __name__ == '__main__':
    cctv = Cctv()
    cctv.get_cctv()
