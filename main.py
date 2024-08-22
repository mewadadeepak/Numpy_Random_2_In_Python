#Seaborn:-

'''
#Plotting a Distplot:
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot([0, 1, 2, 3, 4, 5])

plt.show()               '''

'''
#Plotting a Distplot Without the Histogram:
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot([0, 1, 2, 3, 4, 5], hist=False)

plt.show()                           '''

'''
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot([0, 1, 2, 3, 4, 5], hist=False)

plt.show()                            '''

'''
#Generate a random normal distribution of size 2x3:
from numpy import random

x = random.normal(size=(2, 3))

print(x)                                           '''

'''
#Generate a random normal distribution of size 2x3 with mean at 1 and standard deviation of 2:
from numpy import random

x = random.normal(loc=1, scale=2, size=(2, 3))

print(x)                        '''

'''
#Binomial Distribution:
from numpy import random

x = random.binomial(n=10, p=0.5, size=10)

print(x)                          '''

'''
#Visualization of binomial distribution:
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.binomial(n=10, p=0.5, size=1000), hist=True, kde=False)

plt.show()                             '''

'''
# Normal VS Binomial Distribution:
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.normal(loc=50, scale=5, size=1000), hist=False, label='normal')
sns.distplot(random.binomial(n=100, p=0.5, size=1000), hist=False, label='binomial')

plt.show()               '''


#poission Distribution:

'''
#Generate a random 1x10 distribution for occurrence 2:
from numpy import random
x = random.poisson(lam=2, size=10)

print(x)                    '''


#Visualization of Poisson Distribution:

'''

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.poisson(lam=2, size=1000), kde=False)

plt.show()                      '''



'''
#Normal VS Poisson Distribution:

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.normal(loc=50, scale=7, size=1000), hist=False, label='normal')
sns.distplot(random.poisson(lam=50, size=1000), hist=False, label='poisson')

plt.show()                      '''

'''
#Binomial and Poisson Distribution:
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.binomial(n=1000, p=0.01, size=1000), hist=False, label='binomial')
sns.distplot(random.poisson(lam=10, size=1000), hist=False, label='poisson')

plt.show()              '''

'''

#normal Distribution VS Binomial Distribution VS Poisson Distribution :

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.normal(loc=50, scale=7, size=1000), hist=False, label='normal')
sns.distplot(random.binomial(n=1000, p=0.01, size=1000), hist=False, label='binomial')
sns.distplot(random.poisson(lam=10, size=1000), hist=False, label='poisson')

plt.show()                                  '''


#Uniform Distribution:-

'''
#Create a 2x3 uniform distribution sample:

from numpy import random

x = random.uniform(size=(2, 3))

print(x)                            '''


'''

#Create a 2x3 uniform distribution sample:

from numpy import random

x = random.uniform(size=(2, 3))

print(x)                                      '''


'''
#Visualization of Uniform Distribution

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.uniform(size=1000), hist=False, label='uniform')

plt.show()                                                 '''



#Logistic Distribution:

'''
#Draw 2x3 samples from a logistic distribution with mean at 1 and stddev 2.0:

from numpy import random

x = random.logistic(loc=1, scale=2, size=(2, 3))

print(x)                                       '''


'''
#Visualization of Logistic Distribution:

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.logistic(size=1000), hist=False)

plt.show()                            '''


#Multinomial Distribution:
#Draw out a sample for dice roll:

from numpy import random

#n - number of possible outcomes (e.g. 6 for dice roll).
#pvals - list of probabilties of outcomes (e.g. [1/6, 1/6, 1/6, 1/6, 1/6, 1/6] for dice roll).
#size - The shape of the returned arra

x = random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])

print(x)







