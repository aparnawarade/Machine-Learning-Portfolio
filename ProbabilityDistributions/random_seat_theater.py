#Mark was first to arrive at a 100 seat theater. He forgot his seat number and picked a random seat for himself. 
#After this, every single person who gets to the theater sits on his/her seat if it is available, and chooses any available seat at random. 
#John was last to enter the theater and 99 seats were occupied. What's the probability that John gets to sit in his own seat? Can we write a simulation to verify the result?

import random
def john_get_his_seat():
    available_seats = list(range(1,101))
    johns_seat=0
    #print(available_seats)
    
    #mark got his random seat 
    mark_seat=random.choice(available_seats)
    #print(mark_seat)
    available_seats.remove(mark_seat)
    
    #for next 98 indv +1 mark allot seats 
    for i in range(1,99):
        if i in available_seats:
            available_seats.remove(i)
        else:
            johns_seat=random.choice(available_seats)
            available_seats.remove(johns_seat)
    return johns_seat==99
    

no_of_simulations=10000
sucesses=0
for i in range(no_of_simulations):
    if john_get_his_seat():
        sucesses+=1
probability_of_john_getting_his_seat=sucesses/no_of_simulations
print(probability_of_john_getting_his_seat)
