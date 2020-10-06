import pandas as pd
import numpy as np
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
        self.show_corrcoef(population, cctv)
        print('----------- CCTV & POP ----------')
    
        # print(f'CCTV Header: {cctv.head()}')
        # print(f'Population Header: {population.head()}')
        
    
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

    """
        고령자비율과 CCTV 의 상관계수 [[ 1.         -0.28078554]
                                    [-0.28078554  1.        ]] 
        외국인비율과 CCTV 의 상관계수 [[ 1.         -0.13607433]
                                    [-0.13607433  1.        ]]
       r이 -1.0과 -0.7 사이이면, 강한 음적 선형관계,
       r이 -0.7과 -0.3 사이이면, 뚜렷한 음적 선형관계,
       r이 -0.3과 -0.1 사이이면, 약한 음적 선형관계,
       r이 -0.1과 +0.1 사이이면, 거의 무시될 수 있는 선형관계,
       r이 +0.1과 +0.3 사이이면, 약한 양적 선형관계,
       r이 +0.3과 +0.7 사이이면, 뚜렷한 양적 선형관계,
       r이 +0.7과 +1.0 사이이면, 강한 양적 선형관계
       고령자비율 과 CCTV 상관계수 [[ 1.         -0.28078554] 약한 음적 선형관계
                                   [-0.28078554  1.        ]]
       외국인비율 과 CCTV 상관계수 [[ 1.         -0.13607433] 거의 무시될 수 있는
                                   [-0.13607433  1.        ]]                        
    """

    def show_corrcoef(self, population, cctv):
        population['외국인비율'] = 100.0 * population['외국인']/population['인구수']
        population['고령자비율'] = 100.0 * population['고령자']/population['인구수']
        cctv.drop(["2013년도 이전","2014년","2015년","2016년"], 1, inplace=True)
        cctv_population = pd.merge(cctv, population, on='구별')
        cor1 = np.corrcoef(cctv_population['고령자비율'], cctv_population['소계'])
        cor2 = np.corrcoef(cctv_population['외국인비율'], cctv_population['소계'])

        print(f'고령자비율과 CCTV의 상관계수 {cor1}')
        print(f'외국인비율과 CCTV의 상관계수 {cor2}')
        reader = self.reader
        reader.context = reader.context = '/Users/seung/SbaProjects/sba-3-api/crime/saved_data/'
        reader.fname = 'cctv_population.csv'
        cctv_population.to_csv(reader.new_file())

if __name__ == '__main__':
    cctv = Cctv()
    # cctv.get_population()
    cctv.hook_process()