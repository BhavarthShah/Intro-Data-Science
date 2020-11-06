#random
import random
for i in range(5):
    #range implies the number of time the loop will run - here 5 times
    x = random.random()
    #random includes random variables from 0 to 1 but not 1. 0 is included
    #everytime will give different output
    #can be used for probabilistic methods/ monte carlo simulation
    print (x)

#other random function
#random randint -  will take high and low parameter
#returns including the range number itself

y = random.randint(5,10)
#both high and low are can also be included in return

print('\n') #for 1 new blank line in output
print(y)#print also puts new line so two lines left bank

#other random function
#random choice -  returns ONE random variable from list or sequence

k = [1, 3, 6, 9, 20]
j = random.choice(k)
print("\n")
print(j)
