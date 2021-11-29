#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from scipy.linalg import lu
from scipy.linalg import svd

A = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]
             ])

B = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]
             ])

print('Matrix 1 \n', A)
print('\n Matrix 2 \n', B)

y = int(input('Please Choose Which Matrix do you like to decompose!: '))

if y == 1:
    if A.shape[0] == A.shape[1]:
        x = input('Please choose either Eigen or PLU decomposition: ')
        if x.lower() == 'eigen':
            value, vector = np.linalg.eig(A)
            print('Egien Vector: \n', vector)
            print('\n Egien Value: \n', value)
            q = vector
            l = np.linalg.inv(vector)
            r = np.diag(value)
            print('\n Main Matrix: \n', q.dot(l).dot(r))
        elif x.lower() == 'plu':
            P, L, U = lu(A)
            print('P Part: \n', P)
            print('\n L Part: \n', L)
            print('\n U Part: \n', U)
            print('\n Main Matrix: \n', P.dot(L).dot(U))
else:
    z = input('Please choose either SVD or QR decomposition: ')
    if z.lower() == 'QR':
        Q, R = np.linalg.qr(B, 'complete')
        print('Q Part: \n', Q)
        print('\n R Part: \n', R)
        print('\n Main Matrix: \n', Q.dot(R))
    elif z.lower() == 'SVD':
        U, S, V = svd(B)
        print('U Part: \n', U)
        print('\n S Part: \n', S)
        print('\n V Part: \n', V)


# In[ ]:




