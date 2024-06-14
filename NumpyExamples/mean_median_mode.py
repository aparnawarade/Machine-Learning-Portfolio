import numpy as np 
import matplotlib.pyplot as plt
%matplotlib inline  
##displays the grafts in same window insade of opening new one 

m=np.random.randint(7,10,20)
## gives random values between 7(included) and 10(Excluded) and 20 values 
print(m)

##mean : avg of all observed values 
mean_ =np.mean(m)
print(mean_)

#median is middle value of data distribution 
median_=np.median(m)
print(median_)

#mode : frequently occouring value 
from statistics import mode 
mode_=mode(m)
print(mode_)
