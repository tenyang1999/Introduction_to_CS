input_number = int(input("Input the range number："))

# 重 0 開始計算每一個數值是否為perfect number
for target in range(1,input_number+1):
    
    count_value = 0
    # 去計算是否可以被cnt整除 
    cnt = 1

    while cnt < target+1:
        
        # 如果能夠整除，則加上 target 以及 被除之後的因數值
        if target %cnt == 0 :
            count_value += cnt
            count_value += target/cnt
             
        cnt += 1
    
    #　因為由 1 算到 target值，所以所有因數會重複計算2次要除掉
    #  再扣除 target 值才會是設定的 perfect number
    count_value = (count_value/2) - target
    
    if count_value == target:
        print(target)
        
        
'''<output>
Input the range number：10000
6
28
496
8128
'''