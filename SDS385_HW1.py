import matplotlib.pyplot as plt
from numpy import random

mean1=[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1] #for class 1, 19 elements
mean2=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1] #for class 2, 19 elements

cov=numpy.identity(19)

x= random.multivariate_normal(mean1, cov, 5000)
