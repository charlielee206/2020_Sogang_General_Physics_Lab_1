#https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot
# 이거는 프로그램 짜는거보다 쓰는게 더 힘듦. 항목이 몇 없을때 써. 
# 아니면 이거갖고 씹고뜯고맛보고즐겨서 matplotlib 함수가 어떻게 돌아가는지를 알아보던가

import matplotlib.pyplot as plt
import numpy as np

# 그래프 크기. fig= plt.figure(figsize=(x방향 길이,y방향 길이)). 이거 주석처리하면 자동으로 그려짐.
fig= plt.figure(figsize=(10,3))

# 그래프 화이트스페이스 간격. 없어도 되긴 함. 문제생기면 이거 주석처리
plt.gcf().subplots_adjust(bottom=0.15)

# plt.plot([x1, x2, x3 ..... ], [y1, y2, y3 .....], 'ro', label = '라벨이름', markersize = 5) 
plt.plot([10, 30, 50], [0.65, 0.98, 1.22], 'ro', label = 'Run #1', markersize = 5) 
plt.plot([10, 30, 50], [0.74, 1.09, 1.35], 'bo', label = 'Run #2', markersize = 5)
plt.plot([10, 30, 50], [0.68, 1.02, 1.28], 'co', label = 'Avg', markersize = 5)

#plt.axis([x 최소, x 최대, y최소, y 최대])
plt.axis([0, 60, 0, 2.0])

plt.xlabel('Distance') # x축 이름
plt.ylabel('Force') # y 축 이름
plt.title('Spring 1: Distance vs Force') # 그래프 이름

# 뒤에 모눈선 그리는거
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.minorticks_on()
plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)

# 라벨명 리스트 그리는거
plt.legend(fontsize = 8)

# 마지막에 전체적으로 위의 설정을 표시하는거
plt.show()
