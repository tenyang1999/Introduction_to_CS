# 輸入需要的數值
F  = int(input('Input the force:'))
m1 = int(input('Input the mass of m1:'))
r = int(input('Input the distance:'))

# 基本物理數值
G  =  6.67*(10**(-11))
c = 299792458 

#　計算公式
m2  = F*(r**2)/G/m1
E = m2*(c**2)

# 輸出結果
print('The mass of m2 = ',m2)
print('The energy of m2 =',E)


''' <output>
Input the force:5000
Input the mass of m1:500
Input the distance:50
The mass of m2 =  374812593703148.44
The energy of m2 = 3.3686475964648337e+31
'''
