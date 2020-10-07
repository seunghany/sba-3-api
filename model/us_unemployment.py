import pandas as pd
import numpy as np
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
baseurl = os.path.dirname(os.path.abspath(__file__)) # c:\Users\seung\SbaProjects\sba-3-api\model
from util.file_helper import FileReader
import folium

class UsUnemployment:

    def __init__(self):
        print(f'baseurl ### {baseurl}')
        self.reader = FileReader()

    def show_map(self):
        print('----------- CRIME & POLICE ----------')
        # csv_to_df(self) -> object:
        reader = self.reader
        reader.context = os.path.join(baseurl,'data/')
        reader.fname = 'usa_map.json'
        reader.new_file() # 왜 필요한지 잘 모르겠음.. 이거 유틸에 있지 않나??
        usa_map = reader.json_load() # file 만드는거 내장되 있음
        reader.fname = 'us_unemployment.csv'
        reader.new_file() # 왜 필요한지 잘 모르겠음.. 이거 유틸에 있지 않나??
        us_unemployment = reader.csv_to_df() # file 만드는거 내장되 있음
        print(f'{us_unemployment.head()}')

        map = folium.Map(location=[37, -102], zoom_start=5)
        map.choropleth(
            geo_data = usa_map,
            name = 'choropleth',
            data = us_unemployment,
            columns = ['State','Unemployment'],
            key_on = 'feature.id',
            fill_color = 'YlGn',
            fill_opacity = 0.7,
            line_opacity = 0.2,
            legend_name = 'Unemployment Rate (%)'

        )
        folium.LayerControl().add_to(map)
        reader = self.reader
        reader.context = os.path.join(baseurl,'saved_data/')
        reader.fname = 'usa.html'
        map.save(reader.new_file())
        


if __name__ == '__main__':
    u = UsUnemployment()
    u.show_map()
    