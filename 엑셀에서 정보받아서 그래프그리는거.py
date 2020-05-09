# 엑셀 그래프 기능이 X같아서 만든 그래퍼. 일반실험과목 그래프 이걸로 그리셈.
# 난 1학기 싸강이라 이거 다 혼자서 만들었다;; 게다가 내 주요 언어는 C++ 이라서 파이던 스크립트 짜는게 디게 어색하다
# 이거 만드는데 존나 힘들었다;; 그니까 나중에 맛난거 사줘라.

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

fig= plt.figure(figsize=(10,5)) #그래프 크기. fig= plt.figure(figsize=(x방향 길이,y방향 길이))
plt.gcf().subplots_adjust(bottom=0.15)


# 파일 설정. 이때 파이던 프로그램하고 엑셀파일하고 같은 폴더에 있어야함.
# df = pd.read_excel('엑셀파일_이름.xlsx','시트_이름')
# 이름/항목명등은 ' ' 안에 있어야함.

df = pd.read_excel('테스트 액셀.xlsx','코레가 시트 이름데스')


# plt.plot(df['x축 항목명'],df['y축 항목명'], 'rd', label = '라벨 이름', markersize=4)

# 항목명은 엑셀에서 가장 위에(1행)있어야함.
# rd/ro/r^/md/cd : 그래프 모양. 첫번째 문자는 색, 2번째 문자는 모양. ex) rd : 빨간 다이아, k^ : 검정 삼각형
# r(빨강)/g(초록)/b(파랑)/c(청록)/m(마젠타)/y(노랑)/k(검정). color 함수로 그 외 색 지정 가능. 
# d(다이아)/o(동그라미)/^(삼각형) 그 외 더 있는데 쓰기 귀찮아ㅏㅏㅏ
# markersize=숫자 에서 뒤에 숫자는 그 무늬 크기

plt.plot(df['시간이 됬던'],df['위치가 됬던'], 'rd', label = 'name 1', markersize=3)
plt.plot(df['시간이 됬던'],df['속도가 됬던'], 'ro', label = '이름 2', markersize=3)
plt.plot(df['파이던에서 쓸때'],df['꼭'], 'r^', label = '名 3', markersize=3)
plt.plot(df['파이던에서 쓸때'],df['제일'], 'md', label = 'имя 4', markersize=3)
plt.plot(df['줄에'],df['있어야'], 'cd', label = '항목 더 필요하면 알아서 이 줄 복붙해서 고쳐', markersize=4)


# labels

plt.xlabel('X Axis Label') # x축 이름 

plt.ylabel('Y Axis Label') # y축 이름

plt.title('아아아아이스크림먹고싶다') # 그래프 이름

plt.legend(loc='upper left', fontsize= 8) #'upper left' 대신 'upper right' 등 딴거 넣으면 라벨 위치가 바뀜. 필요 없으면 이 줄 전체를 주석처리 하던가.

# major grid lines
plt.grid(b=True, which='major', color='#666666', linestyle='-')

# minor grid lines
plt.minorticks_on()
plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)

plt.show()
