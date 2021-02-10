from random import randrange as rand
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


#Store has two items
#Initial quantity of first item = Q1
#Initial quantity of second item = Q2
#Items restocked randomly within 1-4 days
#Purchase request for first item = P1
#Purchase request for second item = P2
# P1 < Q1 always
# P2 < Q2 always

## ASSUMPTION 1 ##
# first item is more popular than the second, so must keep a lot more
# initially at 100 and 75 
Q1 = 100
Q2 = 75

## ASSUMPTION 2 ##
# first item restocks 50 items since it sells more quickly 
# second item restocks 25 items
P1 = 50
P2 = 25

#item 1 quantities
item1 = []
item1.append(Q1)

#item 2 quantities
item2 = []
item2.append(Q2)

#100 days
days = [r for r in range(1,26)]

#purchase request notifiers
pn1 = 0
pn2 = 0

#purchase order random day counters
days1 = 0
days2 = 0

for _ in range(1, len(days)):
    ## ASSUMPTION 3 ##
    # item 1 gets bought in a range of 10-17 times a day
    if Q1 > 0:
        if 10 < Q1 <= 18:
            Q1 -= rand(10, Q1 + 1)
        elif Q1 <= 10:
            Q1 = 0
        else:
            Q1 -= rand(10, 18)
    # item 2 gets bought in a range or 5-9 times a day
    if Q2 > 0:
        if 5 < Q2 <= 10:
            Q2 -= rand(5, Q2 + 1)
        elif Q2 <= 5:
            Q2 = 0
        else:
            Q2 -= rand(5,10)
    
    #counts down days until purchase request arrives
    if days1 > 0:
        days1 -= 1
    if days2 != 0:
        days2 -= 1
    
    ## ASSUMPTION 4 ##
    # when Q1 goes below 40, a purchase request is placed
    if Q1 < 40 and pn1 == 0:
        pn1 = 1
        #counter randomly decides how many days until purchase order arrives
        days1 = rand(1,5)
    # when Q2 goes below 20, a purchase request is placed
    if Q2 < 20 and pn2 == 0:
        pn2 = 1
        #counter randomly decides how many days until purchase order arrives
        days2 = rand(1,5)
      
    #when days = 0 and pn = 1, this means that the restock has arrived
    if days1 == 0 and pn1 == 1:
        Q1 += P1
        pn1 = 0
    if days2 == 0 and pn2 == 1:
        Q2 += P2
        pn2 = 0
        
    item1.append(Q1)
    item2.append(Q2)
    
        
print(item1)
print(item2)

dfs = pd.DataFrame(data = {'days': days,
                           'Item 1': item1,
                           'Item 2': item2})

dfs1 = pd.melt(dfs, id_vars='days')

print(dfs1)

plot = sns.catplot(x = 'days', y = 'value', hue = 'variable', data = dfs1, kind = 'bar', height=6)
plot.set(xlabel = 'Day')
plot.set(ylabel = 'Quantity')
plot.legend.set(title = 'Items:')
plot.set(title = 'Item Quantaties After Each Day')   
plot.savefig('Q2')