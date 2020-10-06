import pandas as pd
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from util.file_handler import FileReader

class Crime:
    def __init__(self):
        print(f'hello')
        self.reader = FileReader()
    
    def get_crime(self):
        reader = self.reader
        reader.context = '/Users/seung/SbaProjects/sba-3-api/crime/'
        reader.fname = 'crime_in_seoul.csv'
        reader.new_file()
        crime = reader.csv_to_df()
        print(f'{crime.head()}')

if __name__ == '__main__':
    crime = Crime()
    crime.get_crime()

# class Crime:
#     def __init__(self):
#         self.fileReader = FileReader()
#         self.context = '/Users/seung/SbaProjects/sba-3-api/crime/'


#     def new_model(self, payload) -> object:
#         this = self.fileReader
#         this.context = self.context
#         this.fname = payload
#         return pd.read_csv(this.context + this.fname, sep =',')

# if __name__ == '__main__':
#     crime = Crime()
#     dframe = crime.new_model('cctv_in_seoul.csv')
#     print(dframe.head())
#     dframe = crime.new_model('crime_in_seoul.csv')
#     print(dframe.head())
