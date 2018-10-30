import numpy as np
#import pandas as pd
import random
#from matplotlib.pyplot import plot

p=500
#n=100000
m=100000

mean_dis=[0 for i in range(500)]

cov=np.identity(500)

#generate X
x_mat=np.random.multivariate_normal(mean_dis, cov, m)
x_mat=np.array(x_mat)

# print "the shape of X matrix is "+str(x_mat.shape)

#generate beta
#### if beta is sparse matrix
beta=[0 for i in range(500)]
#
# for i in range(0,500,20):
#     beta[i]=np.random.normal(0,1)

#### if beta is matrix with random integers
for i in range(0,25):
    beta[i]=np.random.uniform(-0.5,0.5)

beta_orig=np.array(beta)
beta=beta_orig[np.newaxis]
beta=beta.T

# print "the shape of beta is"+str(beta.shape)
# print beta

#generate eplison matrix
eplison=[np.random.normal(0,0.01) for i in range(m)]

eplison=np.array(eplison).T

#print("the shape of eplison is "+str(eplison.shape))

# now we generate y matrix

y_mat=np.array(np.dot(x_mat,beta_orig)+eplison)
y_mat=y_mat[np.newaxis]
y_mat=y_mat.T

# print "shape of y matrix is "+str(y_mat.shape)


first_iter_beta=[]
for k in range(500):
    first_iter_beta.append(np.random.uniform(-0.5,0.5))
first_iter_beta=np.array(first_iter_beta)[np.newaxis].T

# run lasso in Python package
from sklearn import linear_model

runtime=5000

reg=linear_model.Lasso(alpha=0.02,max_iter=runtime,selection='random')
reg.fit(x_mat,y_mat)
coef_beta=reg.coef_
conv_time=reg.n_iter_

# beta_iter=[]
# for r in range(runtime):
#     reg=linear_model.Lasso(alpha=0.02,max_iter=i)
#     reg.fit(x_mat,y_mat)
#     coef_beta=reg.coef_ #type is numpy.array
#     beta_iter.append(coef_beta)

#coef_param=reg.get_params

print(coef_beta)

print("above is beta -------------------------------")

#print(coef_param)

lamb=0.005

#now calculate the objective function over number of iterations
# obj_list=[]
# for num in range(runtime):
#     avg_obj=0
#     for j in range(m):
#         obj_1=y_mat[j]-np.dot(x_mat[j],beta_iter[num])
#         obj_2=np.linalg.norm(obj_1,2)
#         obj_3=obj_2**2
#         obj_4=lamb*np.linalg.norm(beta_iter[num],1)
#         obj=obj_3+obj_4
#         avg_obj=avg_obj+obj
#     avg_obj=avg_obj/m
#     obj_list.append(avg_obj)
#
# print (obj_list)

avg_obj=0
for j in range(m):
    obj_1=y_mat[j]-np.dot(x_mat[j],coef_beta)
    obj_2=np.linalg.norm(obj_1,2)
    obj_3=obj_2**2
    obj_4=lamb*np.linalg.norm(coef_beta,1)
    obj=obj_3+obj_4
    avg_obj=avg_obj+obj
avg_obj=avg_obj/m
print("the objective function is "+str(avg_obj))
print("the objective converges at the "+str(conv_time)+"-th iteration")

import pandas as pd
df_beta=pd.DataFrame(coef_beta)

df_beta.to_csv('C:/jiaocai/Stat Models For Big Data/sklearn_lasso_beta.csv')
