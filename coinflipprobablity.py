import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random

def probablity (n,size,p=0.5):
    x=random.binomial(n=n,p=p,size=size)
    sns.displot(x)
    plt.show()
    return x

print("""Hello User :)
Lets find the probablity of coinflip or dice or cards or random """)
print("""
INSTRUCTIONS:
[1. Tries is the number of tries in one experiment]
[2. Experiments is the number of experiment you are gonna perform]
[3. For fair coinflip, the probability of heads and tails is automatically set to 0.5]
[4. The graph shows the success probability of the coin flip]
[5. Enjoy]
""")

N=int(input("Enter Tries : "))
SIZE=int(input("Enter the number of Experiments : "))

probablity(N,SIZE)