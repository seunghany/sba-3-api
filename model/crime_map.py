import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
baseurl = os.path.dirname(os.path.abspath(__file__))
from util.file_helper import FileReader
from model.police import Police

class CrimeMap:

    def __init__(self):
        print(f'baseurl ### {baseurl}')
        self.reader = FileReader()

    def hook_process(self):
        print('----------- POLICE ----------')
        police = Police()
        police_norm = police.get_police_norm() # Normalization 데이터를 정규화