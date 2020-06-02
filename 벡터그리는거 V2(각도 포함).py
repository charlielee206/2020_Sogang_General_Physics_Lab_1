# 각 표시하는 버전. 각 숫자의 위치는 수동으로 조절해야함. 자동으로 하려했는데 일이 너무 커짐. 파이던에서는 탭 여러개 나누는 법도 모르고.
# 으으아아아아아ㅏ 각 표시하는게 왤케 어렵냐아아아ㅏ냐아아앙

# Edit 1: 햐 이거 다 만들고 보니까 그릴필요 없이 손으로 그려서 올리라 하네 씨ㅣㅣㅓㄷ쟈녈ㄷ져고혀ㅓㅏ조ㅓㅏㅑㅕㅐㅛㅇㄱㄷㅅ
# 하 진짜 나 5시간동안 뭐한거냐ㅏㅏ랄더랴ㅏㄷㅈㄴ햐ㅕㅏㅠㄷㄹㄷㅇㅈ노혀ㅑㅏ
# 귀멸의칼날도봐야하는데에에에ㅔㅔㅔㅔ
# 그래도 언젠가는 쓸일이 있기를 바라며 남겨둡니다.

# Edit 2: 오오오오오오오ㅗㅗㅗ오옹오ㅗㅇdhdhdhdhhdhdhdhdhhdㅇ오오ㅗ 물어봤는데 컴으로 벡터 그려도 된다네! 아하하하ㅏㅎ하ㅏ하하하하하하하하하하핳ㅎ하하하하

# Edit 3: 귀멸의 칼날 꿀잼

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import math

X = np.array((0))
Y= np.array((0))

#------여기 아래에 값 넣으면 됨----------

a = 54.5 # 벡터 1 의 x 성분. 
b = 0    # 벡터 1 의 y 성분. 걍 0으로 두자....제바ㄹ

# 참고로 b =! 0 이면 터질수도 있음. 실험 안해봤고 해보기도 싫어. 코드 고치기 그ㅟ찮아앙

Vector_2_Length = 59.8 # 벡터 2 의 크기.

A_B_Angle = 91 # 벡터 1과 벡터 2 사이 각. 

name_1 = 'm1' # 벡터 1 이름
name_2 = 'm2' # 벡터 2 이름
name_3 = 'm3' # 벡터 3 이름. 글고 이름들은 "  " 나 ' ' 안에 넣어야함.

significant = 2 # 유효숫자 표시. 소숫점 몇번째 자리에서 반올림하는가를 표현


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

angle_1 = round(float(angle_of_vectors(a,b,c,d)),significant)
angle_2 = round(float(angle_of_vectors(a,b,-e,-f)),significant)
angle_3 = round(float(angle_of_vectors(c,d,-e,-f)),significant)

angle_plot_1 = mpatches.Arc([0, 0], 15, 15, 0, 0, angle_1)

angle_plot_21 = mpatches.Arc([0, 0], 13, 13, -angle_2, 0, angle_2)
angle_plot_22 = mpatches.Arc([0, 0], 11, 11, -angle_2, 0, angle_2)

angle_plot_31 = mpatches.Arc([0, 0], 9, 9, angle_1, 0, angle_3)
angle_plot_32 = mpatches.Arc([0, 0], 10, 10, angle_1, 0, angle_3)
angle_plot_33 = mpatches.Arc([0, 0], 11, 11, angle_1, 0, angle_3)

label_1 = str(name_1) + ' = ' + str(calculateDistance(0,0,a,b))
label_2 = str(name_2) + ' = ' + str(calculateDistance(0,0,c,d))
label_3 = str(name_3) + ' = ' + str(round(calculateDistance(0,0,e,f),significant))

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
text_2 = str(angle_2) + '°'
text_3 = str(angle_3) + '°'

plt.text(7,5, text_1) # 벡터 1--2 각도 표시. 7,5,가 글씨의 x,y좌표. 알아서 옮겨
plt.text(7,-7, text_2) # 벡터 1--3 각도 표시. 7,-7,가 글씨의 x,y좌표. 알아서 옮겨
plt.text(-20,2, text_3) # 벡터 2--3 각도 표시. -20,2,가 글씨의 x,y좌표. 알아서 옮겨

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

#plt.title('Gurafu no na wa.')

plt.show()
