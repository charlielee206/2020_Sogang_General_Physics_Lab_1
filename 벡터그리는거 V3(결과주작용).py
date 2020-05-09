# 기끔씩 이론과 현실사이에 괴리가 생길때가 있죠. 그때는 현실부정을 하면 됩니다. 그래서 만들엇습니다. 주작버전. 데이터를 마음껏(그러나 걸리지 않게 조심조심) 조작하십시오!

# 주작버전. A_C_Angle 값을 이용한 계산을 통해 그림을 그리지만, 벡터의 크기, 각의 크기 등 표시는 직접 입력하는거. 
# https://www.youtube.com/watch?v=QUXKib-jfEM 처럼 유투브 링크 있는데에다가는 뭘 넣어도 상관없음. 걍 표시용이라. 유튜브 링크 대신 원하는 숫자를 넣으면 됨.
# 아 글고 저 노래들은내가 개인적으로 좋아하는 노래들임. 그 외에는 별 의미 없음. 뭘 넣어도 된다는것을 보여주기 위한거.

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import math


X = np.array((0))
Y= np.array((0))

#------여기 아래에 값 넣으면 됨----------

a = 49.5 # 벡터 1 의 x 성분. 여기서는 49.5. 계산에 쓰이는 숫자.
b = 0    # 벡터 1 의 y 성분. 걍 0으로 두자....제바ㄹ
# 참고로 b =! 0 이면 터질수도 있음. 실험 안해봤고 해보기도 싫어. 코드 고치기 그ㅟ찮아앙

Vector_2_Length = 49.8 # 벡터 2 의 크기. 여기서는 49.8. 계산에 쓰이는 숫자.

A_B_Angle = 120 # 벡터 1과 벡터 2 사이 각. 계산에 쓰이는 숫자.
A_C_Angle = '요루시카 - 비와 카푸치노: https://www.youtube.com/watch?v=PWbRleMGagU'  # 벡터 1과 벡터 3 사이 각. 표시용이라 뭐든지 들어가도 됨
B_C_Angle = '술탄 오브 더 디스코 - 사라지는 꿈: https://www.youtube.com/watch?v=7fsavq0mU2k'  # 벡터 2와 벡터 3 사이 각. 표시용이라 뭐든지 들어가도 됨

label_1 = '달의하루 - 염라: https://www.youtube.com/watch?v=jv543Nk5s18' # 벡터 1 이름.
label_2 = '달의하루 - 너로피어오라 https://www.youtube.com/watch?v=3vhA8njtoQg' # 벡터 2 이름.
label_3 = '요루시카 - 그래서 나는 음악을 그만두었다. : https://www.youtube.com/watch?v=KTZ-y85Erus' # 벡터 3 이름. 글고 이름들은 ' ' 안에 넣어야함.

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

def calculateDistance(x1,y1,x2,y2):  
     dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  
     ansdist = round(dist,2)
     return ansdist  

def angle_of_vectors(A,B,C,D):
    
     dotProduct = A*C + B*D
     modOfVector1 = math.sqrt(A*A + B*B)*math.sqrt(C*C + D*D) 
     angle = dotProduct/modOfVector1
     angleInDegree = math.degrees(math.acos(angle))
     return angleInDegree

angle_1 = round(float(angle_of_vectors(a,b,c,d)),2)
angle_2 = round(float(angle_of_vectors(a,b,-e,-f)),2)
angle_3 = round(float(angle_of_vectors(c,d,-e,-f)),2)

angle_plot_1 = mpatches.Arc([0, 0], 15, 15, 0, 0, angle_1)

angle_plot_21 = mpatches.Arc([0, 0], 13, 13, -angle_2, 0, angle_2)
angle_plot_22 = mpatches.Arc([0, 0], 11, 11, -angle_2, 0, angle_2)

angle_plot_31 = mpatches.Arc([0, 0], 9, 9, angle_1, 0, angle_3)
angle_plot_32 = mpatches.Arc([0, 0], 10, 10, angle_1, 0, angle_3)
angle_plot_33 = mpatches.Arc([0, 0], 11, 11, angle_1, 0, angle_3)


fig, ax = plt.subplots()
q = ax.quiver(X, Y, a, b, units='xy' ,scale=1, color= 'r', label=label_1)
r = ax.quiver(X, Y, c, d,units='xy' ,scale=1, color= 'b', label=label_2)
s = ax.quiver(X, Y, e, f,units='xy' ,scale=1, color = 'k') # 합벡터 안 그릴려면 이 줄 주석처리.
t = ax.quiver(X, Y, -e, -f,units='xy' ,scale=1, color = 'g', label=label_3)

ax.add_patch(angle_plot_1)
ax.add_patch(angle_plot_21)
ax.add_patch(angle_plot_22)
ax.add_patch(angle_plot_31)
ax.add_patch(angle_plot_32)
ax.add_patch(angle_plot_33)

text_1 = str(A_B_Angle) + '°'
text_2 = str(A_C_Angle) + '°'
text_3 = str(B_C_Angle) + '°'

plt.text(7,5, text_1) #벡터 1--2 각도 표시. 7,5,가 글씨의 x,y좌표. 알아서 옮겨
plt.text(7,-7, text_2) #벡터 1--3 각도 표시. 7,-7,가 글씨의 x,y좌표. 알아서 옮겨
plt.text(-20,2, text_3) #벡터 2--3 각도 표시. -20,2,가 글씨의 x,y좌표. 알아서 옮겨

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

#plt.title('Run #1')

plt.show()
