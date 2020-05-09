# 하 진짜 벡터도 그려야함 이게 뭐냐 일물실 진짜 드랍각인데 드랍하면 또 나중에 들어야하고 진짜 뭐같다ㅏㅏㅏ
# <strike>벡터를 그리라는데 또 손으로 그리면 감점이래.</strike> 

# Edit 1: 아니ㅣㅣ니니ㅣㅣ니니니니니니ㅣㅇ닝니이이인이이 손으로 그리면 감점이래서 이걸 다 짰는데에ㅔㅐㅔ엔에 갑자기ㅣ 손으로 그리라고 하면 어떠카냐골오오오ㅗㅗㅗㅗ어오오 
# Edit 2: 오오오 컴으로 그려도 된다고 하네! 개ㅐ이ㅣ드ㅡㄱㄱ!!! 오오오호호호호홓

# 그래퍼 말고 이거도 쓰면 맛난거 한번 더 사줘라. 초코 아이스크림 죠아요

import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import math


X = np.array((0))
Y= np.array((0))

#------여기 아래에 값 넣으면 됨----------

a = 49.5 # 벡터 1 의 x 성분
b = 0    # 벡터 1 의 y 성분

A_B_Angle = 120 # 벡터 1과 벡터 2 사이 각. 여기서는 120
Vector_2_Length = 49.8 # 벡터 2 의 크기. 여기서는 49.8

label_1 = 'FA' # 벡터 1 이름
label_2 = 'FB' # 벡터 2 이름
label_3 = 'FC' # 벡터 3 이름.(벡터 3 == 합벡터의 역벡터)


# x,y 축 최대. 최소 표시값. 그래프 잘리면 늘리고 너무 크면 좀 줄여. -80,80/ -60,60 하면 엔간한건 그려짐.
# 고치기 귀찮으면 실행시 뜨는 그래프에서 우클릭+드래그 하면 확대/축소됨.
xmin = -80
xmax = 80
ymin = -60
ymax = 60

# --------------------------------------

c = Vector_2_Length*(math.cos(math.radians(A_B_Angle))) 
d = Vector_2_Length*(math.sin(math.radians(A_B_Angle))) 

e = a + c 
f = b + d 


fig, ax = plt.subplots()
q = ax.quiver(X, Y, a, b, units='xy' ,scale=1, color= 'r', label=label_1)
r = ax.quiver(X, Y, c, d,units='xy' ,scale=1, color= 'b', label=label_2)
s = ax.quiver(X, Y, e, f,units='xy' ,scale=1, color = 'k') # 합벡터 안 그릴려면 이 줄 주석처리.
t = ax.quiver(X, Y, -e, -f,units='xy' ,scale=1, color = 'g', label=label_3)


x_1 = [a, e]
y_1 = [b, f]
x_2 = [c, e]
y_2 = [d, f]

plt.plot(x_1, y_1, 'k--', alpha = 0.7) # 합벡터에서 평햏사변형 점선 안 그리려면 이거 주석처리.
plt.plot(x_2, y_2, 'k--', alpha = 0.7) # 합벡터에서 평행사변형 점선 안 그리려면 이거도 주석처리.


major_ticks = np.arange(-100, 120, 20)
minor_ticks = np.arange(-100, 120, 5)

ax.set_xticks(major_ticks)
ax.set_xticks(minor_ticks, minor=True)
ax.set_yticks(major_ticks)
ax.set_yticks(minor_ticks, minor=True)

ax.grid(which='both')

ax.grid(which='minor', alpha=0.2)
ax.grid(which='major', alpha=1)
ax.set_axisbelow(True)

plt.axis('equal')

plt.axis([xmin, xmax, ymin, ymax]) 

plt.gca().set_aspect("equal")

plt.legend(loc='upper left', fontsize= 8)

#plt.title('Run #1') #그래프 전체 제목

plt.show()