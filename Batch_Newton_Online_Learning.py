#import matplotlib.pyplot as plt
import numpy
from numpy import random

mean1=[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1] #for class 1, 19 elements
mean2=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1] #for class 2, 19 elements

cov=numpy.identity(19)

class1= random.multivariate_normal(mean1, cov, 50000) #class 1 1,000,000
#cla_1=numpy.insert(class1,0,1,axis=1)

class2= random.multivariate_normal(mean2, cov, 50000) #class 1 1,000,000
#cla_2=numpy.insert(class2,0,1,axis=1)

#print(cla_1[0])

#now generate two subsets of train and set

train_xy=[]
for i in range(len(class1)):
	train_xy.append([class1[i],-1])
#print(train_xy[0][0])
for i in range(len(class2)):
	train_xy.append([class2[i],1])
#print(len(train_xy))

test_xy=[]
for i in range(len(cla_1)):
	test_xy.append([cla_1[i],-1])
#print(train_xy[0][0])
for i in range(len(cla_2)):
	test_xy.append([cla_2[i],1])

#train=numpy.concatenate((cla_1,cla_2),axis=0)
#test=numpy.concatenate((cla_1,cla_2),axis=0)
#print(train[0])
#print(len(train))
print('------------------------------')

#now generate 30 permutations
train_list=[]
for i in range(30):
	train1=numpy.random.permutation(train_xy)
	train_list.append(train1)
print(train1[0])
print(len(train_list))

per1=numpy.random.permutation(train_xy)

test_list=[]
for i in range(30):
	test1=numpy.random.permutation(test)
	test_list.append(test1)
#
#now define the least square function and f(x)

import math
def f(x):
	return 1.71*numpy.tanh(0.66*x)

def L(x,y,theta):
	return (1.5*y-f(theta*x))**2

#Batch-Newton Algorithm

#define gradient g
#import sympy
def g(size,train,theta): # g is row column vector
	"""
	size is the sample of training e.g. 1000,2000,5000
	x are taken from train set[20 dimensional vector] # an array
	y are taken from train set[y]=+-1 # an array
	theta_k-1 are the k-th iteration for theta
	"""
	sum_g=numpy.zeros((19,1))
	for i in range(size):
		#L_i=L(train[i][0],train[i][1],theta)
		#par_der=numpy.diff(L_i,theta_k_1)
		par_der=(5643*train[i][0]*((3*train[i][1])/2 - (171*numpy.tanh((33*theta*train[i][0])/50))/100)*(numpy.tanh((33*theta*train[i][0])/50)**2 - 1))/2500
		#print('shape')
		par_der1=numpy.array(par_der)
		#print(par_der1.shape)
		# par_der2=par_der1.transpose()
		par_der2=numpy.array(par_der1)[numpy.newaxis]
		par_der3=par_der2.transpose()
		#print(par_der2.shape)
		#print(par_der3.shape)

		sum_g=numpy.array(sum_g)+par_der3
		#print(sum_g.shape)
		#print(sum_g.shape)
	return sum_g #19*1 matrix

#define Hessian matrix
def H(size,theta_k_1,x): #size is the train size
	#s1=(19,19)
	sum_h = numpy.zeros((19,19))
	# print(sum_h.shape)
	# print('sum size')
	#print(sum_h.size)
	for p in range(size):
		x_array=numpy.array(x[p][0])[numpy.newaxis]
		# print(x_array.shape)
		x_the_pro=numpy.dot(numpy.array(theta_k_1),x_array)
		# print(x_the_pro.shape)
		#h1_i=numpy.diff(f(numpy.dot(theta_k_1,x[p])))
		h1_i=-(5643*x[p][0]*(numpy.tanh((33*theta_k_1*x[p][0])/50)**2 - 1))/5000
		# print(h1_i.shape)
		#h1_i=1.71*0.66*(1-(numpy.tanh(0.66*numpy.dot(theta_k_1,x[p][0])))**2)*x[p][0] #row vector
		h1_i=numpy.array(h1_i)
		h2_i=h1_i.transpose()

		h_i=numpy.multiply(numpy.array(h2_i),numpy.array(h1_i))

		sum_h=sum_h+h_i
	return sum_h #19*19 matrix

#run iteration using Newton's formula
def iteration(theta,size,train):
	#train_x=[item[0] for item in train_xy]
	#train_y=[item[1] for item in train_xy]
	diff_norm=numpy.linalg.norm(theta)

	while diff_norm>=(0.01/size):
		#the_norm=numpy.linalg.norm(theta)
		#diff_of_norm=diff_norm-the_norm

		try:
		    H_inv=numpy.linalg.inv(H(size,theta,train))

		except numpy.linalg.LinAlgError:# Not invertible. Skip this one.
		    pass
		else:
			gi=g(size,train,theta)
			hinv_g=numpy.dot(numpy.array(H_inv),numpy.array(gi))
			# theta=theta-H_inv*g(size,train,theta)

			theta=theta-hinv_g
			# print(theta.shape)
			the_norm=(numpy.linalg.norm(theta))
			diff_norm=abs(diff_norm-the_norm)
			print('diff of norm is'+str(diff_norm))
	return theta

#Online algorithm

def learn_alg(size,x,y,theta,scal_mat): #x is row vector
	for t in range(size):
		scalar=max(20,t-40)
		L_dtheta=numpy.diff(L(x[t],y[t],theta))
		try:
			scal_mat_inv=numpy.linalg.inv(scal_mat)
		except numpy.linalg.LinAlgError:# Not invertible. Skip this one.
			pass
		else:
		    #scal_mat_inv=numpy.linalg.inv(scal_mat)
		    h1_t=sympy.diff(f(theta_k_1*x[p]),theta_k_1)
		    h2_t=h1_t.transpose()
		    h_t=h1_t*h2_t
		    scal_mat1=(1-2/scalar)*scal_mat_inv+(2/scalar)*h_t
		    scal_mat=numpy.linalg.inv(scal_mat1)
		    theta=theta-1/scalar*scal_mat*L_dtheta
		return theta

theta_test=numpy.random.uniform(-0.5,0.5,19)
#print(theta_test)
theta_test_t=numpy.array(theta_test)[numpy.newaxis]
theta_test1=theta_test_t.transpose() #theta is column vector

iteration(theta_test1,100,per1)
print(iteration(theta_test1,100,per1))
# print('theta equals')
# print(iteration)

def run_iter_diffsize(size,x,y,theta):
	iteration(theta_test1,size,train_xy)
