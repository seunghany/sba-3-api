import pandas as pd
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from util.file_handler import FileReader

class CrimeModel:
    def __init__(self):
        print(f'hello')
        self.reader = FileReader()
    
        def hook_process(self):
            print("-------------- CRIME & POLICE ------------------------")
            crime = self.get_crime()
            self.get_station(crime)


    def get_crime(self):
        reader = self.reader
        reader.context = '/Users/seung/SbaProjects/sba-3-api/crime/'
        reader.fname = 'crime_in_seoul.csv'
        reader.new_file()
        crime = reader.csv_to_df()
        print(f'{crime.head()}')
        return crime
    
    def get_station(self):
        reader = self.reader
        station_names = []
        for name in crime['관서명']:
            station_names.append('서울'+str(name[:-1]+'경찰서'))
        station_addrs= []
        station_lattitude = [] # 위도
        station_longitude = [] # 경도
        gmaps = reader.create_gmaps()
        for name in station_names:
            t = gmaps.geocode(name, language='ko')
            station_addrs.append(t[0].get('formatted_address'))
            t_loc = t[0].get('geometry')
            station_lattitude.append(t_loc['location']['lat'])
            station_lattitude.append(t_loc['location']['lng'])
            print(name+'------>' + t[0].get('formatted_address'))
        
        gu_names = []
        for name in station_addrs:
            t = name.split()
            gu_name = [gu for gu in t if gu[-1] == '구'][0]
            gu_names.append(gu_name)
        crime['구별'] = gu_names
        print("*****" *20)
        print(crime.head())

        # 구 이름이랑 위치랑 다른곳 맞춰주기
        crime.loc[crime['관서명'] == '혜화서', ['구별']] == '종로구'
        crime.loc[crime['관서명'] == '서부서', ['구별']] == '은평구'
        crime.loc[crime['관서명'] == '강서서', ['구별']] == '양천구'
        crime.loc[crime['관서명'] == '종암서', ['구별']] == '성북구'
        crime.loc[crime['관서명'] == '방배서', ['구별']] == '서초구'
        crime.loc[crime['관서명'] == '수서서', ['구별']] == '강남구'

        crime.to_csv()

if __name__ == '__main__':
    crime = CrimeModel()
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
