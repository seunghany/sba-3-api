import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
baseurl = os.path.dirname(os.path.abspath(__file__))
import numpy as np
import tensorflow as tf 
import tensorflow_datasets as tfds
# pip install tensorflow-datasets
# conda install -c anaconda tensorflow-datasets
import util.version_checker
class Imdb:

    train_data : object = None
    validataion_data : object = None
    test_data : object = None
    model : object = None

    def __init__(self):
        util.version_checker.env_info()

    def hook(self):
        pass

    '''
    훈련 세트를 6대 4로 나눕니다.
    훈련에 15,000 개 샘플, 검증에 10,000개 샘플, 테스트에 25,000 샘플 사용
    '''
    def get_data(self):
       self.train_data, self.validation_data, self.test_data = tfds.load(
                                    name="imdb_reviews", 
                                    split=('train[:60%]', 'train[60%:]', 'test'),
                                    as_supervised=True)

    '''
    샘플생성
    데이터셋이 많으므로 GD 보다는 mini-batch 방식을 사용합니다.
    '''
    def create_sample(self) -> object:
        return None

    '''
    모델 생성
    '''
    def create_model(self):
        self.model = model

    '''
    모델 훈련
    '''
    def train_model(self):
        self.model.fit()

    '''
    모델 평가
    '''
    def eval_model(self):
        self.model.evaluate() 

    '''
    모델 디버깅
    '''
    def debug_model(self):
        print(f'self.train_data : {self.train_data}')
        print(f'self.validataion_data : {self.validataion_data}')
        print(f'self.test_data : {self.test_data}')

if __name__ == '__main__':
    api = Imdb()
    # api.get_data()
    api.debug_model()
    