"""
ann, dnn, 

nn = (bool 함수  + 활성화함수 + 계단함수) , (), ()
cost function
ann, anns = dnn, dnn + col => cnn


프레임워크 vs 라이브러리

use 라이브러리(디펜던시)



function y = WX + b 1943

pn 활성화함수 exists(계단함수)

y = f(y = WX + b) 0, 1 -> pn
ai winter

adalin 0.0 ~ 1.0


텐서플로 는 라이브러리다. TF is Lib.
플라스크 는 프레임워크다
케라스는 API 다

TF : CPU, GPU(CUDA)

TF 는 알고리즘을 구현, 실행, 인터페이스 를 가지고 있다. TF has interface.

저수준 : 자유도 높다
고수준 : 자유도 낮다 -> 개발자가 커스터마이징할 요소가 적다...

노드 : 입력과 출력을 가지는 연산 = 함수 (그래프 = matrix)
세션 넣어서 실행
즉시실행모드 (세션을 히든)

텐서는 스칼라, 벡터, 매트릭스등이 일반화 한 것
스칼라: 랭크 0 인 텐서
벡터 : 랭크 1인 텐서
매트릭스 : 랭크 2 텐서
큐빅 : 랭크 3 텐서
? : 랭크 4 텐서
? : 랭크 5 텐서


선형대수학에서, 
다중선형사상(multilinear map)또는 텐서(tensor)는 
선형 관계를 나타내는 다중선형대수학의 대상이다. 
19세기에 카를 프리드리히 가우스가 곡면에 대한 미분 기하학을 만들면서 도입하였다. 

 텐서는 기저(basis : n_vector)를 선택하여 다차원 배열로 나타낼 수 있으며, 
 기저를 바꾸는 변환 법칙이 존재한다. 

 a = 0
 b = 0.0
 c = '0'

랭크는 차원의 단위다.

variable

Variable, Const, placeholder

placeholder : 저수준으로 개발할 때 , 입력데이터 , 하이퍼파라미터 튜닝을 하는 곳
Weight D-2

dnn = bool 함수  + 활성화함수 + 손실함수 + 옵티마이저 

손실함수를 안다는 것의 의미 ?

self.w = tf.Variable(tf.zeros(shape=(1)))
self.b = tf.Variable(tf.zeros(shape=(1)))

"""