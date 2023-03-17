year = int(input("Please enter a year:"))

# 先判斷是否可以被4整除，否則非閏年
if year%4 == 0:
    # 判斷是由出現機率最小的排在前面
    if year%400 == 0 :
      print("It's a leap year!")
    elif year%100 == 0 :
      print("It's not a leap year.")
    else:
      print("It's a leap year!")
else:
    print("It's not a leap year.")
    
# 判斷是否是西元或西元前
if year > 0:
    print(year,"AD")
else :
    print(year,'BC')