import pandas as pd
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from util.file_handler import FileReader

class Cctv:
    def __init__(self):
        print(f'hello')
        self.reader = FileReader()
    
    def hook_process(self):
        print("-------------- CCTV & POP ------------------------")
        cctv = self.get_cctv()
        population = self.get_population()

        print(f'CCTV Header: {cctv.head()}')
        print(f'Population Header: {population.head()}')
        
    
    def get_cctv(self):
        reader = self.reader
        reader.context = '/Users/seung/SbaProjects/sba-3-api/crime/'
        reader.fname = 'cctv_in_seoul.csv'
        reader.new_file()
        cctv = reader.csv_to_df()
        # print(f'{cctv.head()}')
        cctv.rename(columns = {cctv.columns[0]: "구별" }, inplace = True)
        cctv.dropna(inplace=True) # There's no null file but just incase for the future addition
        return cctv

    def get_population(self):
        reader = self.reader
        reader.context = '/Users/seung/SbaProjects/sba-3-api/crime/'
        reader.fname = 'pop_in_seoul.xls'
        reader.new_file() # return self.context + self.fname
        population = reader.xls_to_df(2, 'B,D,G,J,N')
        # print(f'{population.head()}')
        population.rename(columns = {
            population.columns[0]: "구별",
            population.columns[1]: "인구수",
            population.columns[2]: "한국인",
            population.columns[3]: "외국인",
            population.columns[4]: "고령자"
        }, inplace = True)
        population.dropna(inplace=True)
        return population


if __name__ == '__main__':
    cctv = Cctv()
    # cctv.get_population()
    cctv.hook_process()