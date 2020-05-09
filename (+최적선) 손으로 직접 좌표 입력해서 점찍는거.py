# 최적선 그리는거 포함. 수치는 여전히 손으로 입력해야함.
# 진짜 엑셀 입력 + 최적선은 안나왔으면 좋겠다 진짜....
# 아니 솔직히 엑셀 입력은 별로 안 어렵고... 벡터는 진짜 더이상 하기 싫다. 벡타 씨바ㅏㄹ

# 지금 이 프로그램은 값 + 최적선 하나인더 혹시 한 그래프에 선을 여러개 그려야하면... 알아서 복붙하고 변수 바꿔요. 귀찮아서 못하겠음

import matplotlib.pyplot as plt
import numpy as np
import math

# 그래프 크기. fig= plt.figure(figsize=(x방향 길이,y방향 길이)). 이거 주석처리하면 자동으로 그려짐.
#fig= plt.figure(figsize=(10,3))

# 그래프 화이트스페이스 간격. 없어도 되긴 함. 문제생기면 이거 주석처리
plt.gcf().subplots_adjust(bottom=0.15)

#-------여기에 값 입력해요오오----------------

#x,y 값들. [x1, x2, x3, x4....] / [y1, y2, y3, y4.....] 이따구로 감.
x1 = np.array([0.025, 0.035, 0.042, 0.051, 0.06])
y1 = np.array([0.234, 0.268, 0.302, 0.336, 0.370])

#--------------------------------------------

slope1, intercept1 = np.polyfit(x1, y1, 1)

display_slope_1 = round(float(slope1), 2)

plt.plot(x1, slope1*x1 + intercept1, label = 'slope = ' + str(display_slope_1), color = '#ff8340',linestyle = '-', linewidth = 2.5)

plt.plot(x1, y1, 'rd', markersize = 6) 

#--------------------------------------------

#plt.axis([x 최소, x 최대, y최소, y 최대])
plt.axis([0, 0.065, 0, 0.6])

plt.xlabel('Distance') # x축 이름
plt.ylabel('Force') # y 축 이름
plt.title('Spring : Distance vs Force') # 그래프 이름

# 뒤에 모눈선 그리는거
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.minorticks_on()
plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)

# 라벨명 리스트 그리는거
plt.legend(fontsize = 8)

# 마지막에 전체적으로 위의 설정을 표시하는거
plt.show()
