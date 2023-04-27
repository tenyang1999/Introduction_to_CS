row = int(input('Enter the number of rows: '))
col = int(input('Enter the number of columns: '))
reserve = input('Enter the reserved seats: ')

reserve = reserve.split("|")
out_of_range = []
seat = [list('A')*col for i in range(row)]

for i in range(len(reserve)):
    reserve[i] = reserve[i].split(',')
    
for i, j in reserve:
    if int(i) == 0 or int(j) == 0 :
        out_of_range.append(f"{i},{j}")
    try:
        seat[int(i)-1][int(j)-1] = 'R'
    except IndexError :
        out_of_range.append(f"{i},{j}")

print("Out - of - range reserved seats:","|".join(out_of_range))
print("Seating Arrangemnet:")
for i in seat:
    for j in i:
        print(j, end=" ")
    print()