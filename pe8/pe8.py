import csv

nba = []
with open("./nba_standings.csv", "r") as csvfile:
    reader_variable = csv.reader(csvfile, delimiter=",")
    for row in reader_variable:
        nba.append(row)
        
wlp = [] #win-loss percentage
for i in range(1,len(nba)):
    if nba[i][0] == 'Eastern' and float(nba[i][3])>0.5:
       wlp.append(nba[i][1]) 
print("The team where win-loss percentage greater than 0.5 is ",wlp)

lwr = [] #lower win rate
for i in range(1,len(nba)):
    if nba[i][0] == 'Western':
        home = list(map(int,nba[i][7].split("-")))
        home = home[0]/sum(home)
        away = list(map(int,nba[i][8].split("-")))
        away = away[0]/sum(away)
        if home < away:
            lwr.append(nba[i][1]) 
print("The team from the Western Conference had a lower win rate at home games compared to their away games is",lwr)

diff_avg= []
for i in range(1,len(nba)):
    if nba[i][0] == 'Eastern' and float(nba[i][3])>0.5:
       diff =  float(nba[i][5])-float(nba[i][6])
       diff_avg.append(diff)
print("The average difference between PF and PA for team is",round(sum(diff_avg)/len(diff_avg),4))