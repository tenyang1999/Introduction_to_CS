# 輸入input值
h = int(input('Input the height of the 1st ball:'))
m1 = int(input('Input the mass of the 1st ball:'))
m2 = int(input('Input the mass of the 2nd ball:'))

g = 9.8

# U = m*g*h ，計算位能
U = m1*g*h

# 1st ball m = m1, 碰撞前 = u1, 碰撞後 = v1
# 2st ball m = m2, 碰撞前 = u2, 碰撞後 = v2

u1 = (2*U/m1)**(0.5)

# 碰撞後的速度公式
#v1 = u1*(m1-m2)+(2*m1*u1)/ (m1+m2)
#v2 = u2*(m2-m1)+(2*m1*u1)/ (m1+m2)

v2 = (2*m1*u1)/ (m1+m2)


print('The velocity of the 1st ball after slide: ',u1 ,'  m/s ')
print('The velocity of the 2nd ball after collision:' ,v2 ,' m/s')

'''<output>
Input the height of the 1st ball:100
Input the mass of the 1st ball:10
Input the mass of the 2nd ball:40
The velocity of the 1st ball after slide:  44.27188724235731   m/s 
The velocity of the 2nd ball after collision: 17.708754896942924  m/s
'''