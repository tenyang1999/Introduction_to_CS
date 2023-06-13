# initial statements
s1 = "spam" 
s2 = "ni!" 

# Problem 1‐1
print("The Knights who say," + s2)
print(3 * s1 + 2 * s2)
print(s1[1])
print(s1[1:3])
print(s1[2]+ s2[:2])
print(s1 + s2[-1])
print( s2[len(s2)//2] )

'''<output>

* index 由 "0"開始

The Knights who say,ni!
spamspamspamni!ni!       # 將字串重複
p                        # 取index=1的字元
pa                       # 取index=1-2的字元
ani                      # 取s1 index=2的字元 + s2 index=0-1的字元
spam!                    # s1 + s2最後一個字元 
i                          
'''

# Problem 1‐2

print(str.upper(s2)) 
print(s2+ s1+ s2)
print( (str.upper(s1[0])+ s1[1:]+ str.upper(s2[0])+ s2[1:]) *3)
print(s1[:3]+s2[0])
print(s1[:2]+s1[-1])

'''<output>
NI!
ni!spamni!
SpamNi!SpamNi!SpamNi!
span
spm
'''
# Problem 1‐3

print("Looks like %s and %s for breakfast" % ("spam", "eggs"))
print("There is %d %s %d %s" % (1, "spam", 4, "you"))
print("Hello %s" % ("Suzie", "Programmer") )                    #  因為少一個 %s做佔位符
print("%0.2f %0.2f" % (2.3, 2.3468) )
print("%7.5f %7.5f" % (2.3, 2.3468) )
print("Time left %02d:%05.2f" % (1, 37.374) )
print("%3d" % ("14") )                                          # "14"為str -> %3s

'''<output>
Looks like spam and eggs for breakfast
There is 1 spam 4 you
Hello Suzie Programmer
2.30 2.35
2.30000 2.34680
Time left 01: 37.37
 14


'''
# Problem 1‐4
# a
x = 5 
y = 3 
if x >= y: 
    x = x - 2 
print(x) 
#　3

# b
tc = 100 
tf = (9/5) * tc + 32 
print(tf) 
# 212.0

# c
x = 0 
while x < 5: 
    x = x + 1 
print(x)
# 5

# d
x = 1 
i = 1 
while x <= 5: 
    x = x * i 
    i = i+1 
print(x) 
# 6

# e
x = 0 
while x < 6: 
    if x % 2 == 0: 
        print('even', x) 
    else: 
        print('odd', x) 
    x = x + 1 
# even 0
# odd 1
# even 2
# odd 3
# even 4
# odd 5

# f 
i = 0  
while i < 6:  
    j = 0  
    print(i,j) # 多加一行，可以檢視 i 與 j 的值
    while j < i:  
        print("*") 
        j = j + 1  
    i = i + 1  
    print()

'''
0 0

1 0
*

2 0
*
*

3 0
*
*
*

4 0
*
*
*
*

5 0
*
*
*
*
*
'''

# g

score = 40 
while score > 1:
    score = score/2 - 1  
    print(score) 

# 19.0
# 8.5
# 3.25
# 0.625

# h

x = 2 
y = 7 
while x < y:
    x = 2 * x 
print(x)
# 8

# i
a, b = 63, 105 
while b:  
    a, b = b, a % b 
    print(a,b) # 增加一行去看a,b變化
print(a) 

'''
105 63
63 42
42 21
21 0
21
'''
# j

n = 21 
while n != 1:
    print(n, end=", ")    
    if n % 2 == 0:         
        n = n // 2     
    else:         
        n = n * 3 + 1 
print(n, end=".\n")
# 21, 64, 32, 16, 8, 4, 2, 1.

# Problem 1‐5

# a
x = 7  
y = 8  
if x < 7 or x <= 10 and y > 8:  
    print("ugh") 
else:  
    print("yuck")
#　yuck ， 因為y並不大於8

# b 
phrase = "python" 
vowels = "aeiou" 
count = 0 
while (not phrase[count] in vowels):  #去判斷phrase裡面的字母是否在vowels裡面，若不是則 +1，直到判斷為是
    count = count + 1 
print(count) 
# 4

# c 
if 'alpha' < 'zebra': 
    print('alpha < zebra') 
elif 'alpha' > 'zebra': 
    print('alpha > zebra') 
elif 'alpha' == 'zebra': 
    print('alpha == zebra') 
else: 
    print('none of the above')
    
# 'alpha < zebra' ，是判斷首個字母 a < z


# Problem 1‐6 

'''
1 said he is not the thief. 
2 said 3 is the thief. 
3 said 4 is the thief. 
4 said 3 is a liar. 
'''


