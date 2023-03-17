a = 4.0 / 10.0 + 3.5 * 2 
print('a:',a)
print(type(a))

b = 10 % 4 + 6 / 2 
print('b:',b)
print(type(b))

c = (6.5 - 5.0)**(0.5) + 7 * 3 
print('c:',c)
print(type(c))

d = 3 * 10 / 3 + 10 % 3 
print('d:',d)
print(type(d))

e = 5 / (1 // 2) 

'''<output>

a: 7.4
<class 'float'>
b: 5.0
<class 'float'>
c: 22.22474487139159
<class 'float'>
d: 11.0
<class 'float'>
Traceback (most recent call last):
  File "/home/re6114056/DS_Intro_hw/p1-1.py", line 17, in <module>
    e = 5 / (1 // 2) 
ZeroDivisionError: division by zero
'''