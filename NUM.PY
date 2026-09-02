import numpy as np

#it's create list of zero's
# numpy = np.zeros([4])
# print(numpy)

#it's create list of one
# numpy = np.ones([4])
# print(numpy)

#it's create list of number we want
# numpy = np.full([4],5)
# print(numpy)

# 2D arrays 
# numpy =np.full([2,3],9)
# print(numpy)

# arange is just like range in python
# numpy_array =np.arange(1,20,3)
# print(numpy_array)

#identity matrix
# numpy=np.eye(3)            #np.eye Give 1 in Digonal
# print(numpy)

#import numpy as np
# numpy=np.array([(1,2.8,8),
#                 (4,5,6)])
# int=numpy.astype(int)
# print(int)

# import numpy as np
# numpy=np.array([(1,2.8,8),
                # (4,5,6)])
# print(numpy.shape)

# import numpy as np
# numpy=np.array([(1,2.8,8),
#                 (4,5,6)])
# print(numpy.size)

# import numpy as np
# numpy=np.array([(1,2.8,8),
#                 (4,5,6)])

# print(numpy+6)


# import numpy as np
# numpy=np.array((1,6,8))
# print(np.sum(numpy))
# print(np.mean(numpy))
# print(np.min(numpy))
# print(np.max(numpy))
# print(np.std(numpy))
# print(np.var(numpy))

#Indexing and Slicing
# import numpy as np
# num = ([1,2,3,4,5,6,7,8,9,100])
# print(num[1:5])            #index 1 to 4
# print(num[:5])             #index 0 to 4
# print(num[::5])            # every second element
# print(num[::-5])

# Fancy indexing (selecting multiple elements)
# import numpy as np
# num = np.array([1,2,3,4,5,6,7,8,9,100])
# print(num[[0,3,5]])

# Filttering 
# import numpy as np
# num = np.array([1,2,3,4,5,6,7,8,9,100])
# print(num[num>5])

# Reshaping converting multidimension to 1D
# import numpy as np
# num = np.array([[1,2,3],
#                 [5,9,7]])

# ravel1 = num.ravel()
# print(ravel1)
# fla0tten1 = num.flatten()
# print(fla0tten1)


# Reshaping converting  1D to Multidimension
# import numpy as np
# num = np.array([[1,2,3,6,9,8,4,7,44]])
# reshape=num.reshape(3,3)
# print(reshape)

# Adding a number/insert number
# import numpy as np
# num=np.array([1,23,6,5,8,5,])
# new=np.insert(num,4,100)
# print(new)

# Adding a number/insert number in multi
# import numpy as np
# num=np.array([[1,23,6],
            #  [5,8,5,]])
# new=np.insert(num,1,[4,5,9],axis=0)
# print(new)

# Adding two row
# import numpy as np
# num=np.array([4,1,23,6])
# num1=np.array([5,9,5,6])
# new=np.concatenate((num,num1))
# print(new)

# # REMOVING 
# import numpy as np
# num=np.array([4,1,23,6])
# new=np.delete(num,2)
# print(new)

# # REMOVING 
# import numpy as np
# num=np.array([[4,1,23,6],[8,5,6,3]])
# new=np.delete(num,0,axis=0)
# print(new)

# Spliting
# import numpy as np
# num=np.array([4,1,23,6,8,5,6,3])
# new=np.split(num,2)
# print(new)

# adding the 1D to multi
# import numpy as np

# num=np.array([[4,1,2],
#              [5,9,8]])
# vector=np.array([2,6,8])
# result= num+vector
# print(result)

import numpy as np
# np.isnan    # find a value
# np.nan_to_num     # finding a number
# np.isinf          #for infinity

# num=np.array([7,6,5,np.nan])
# print(np.isnan(num))



# num=np.array([7,6,5,np.nan])
# print(np.nan_to_num(num,nan=4))

# num=np.array([7,6,5,np.inf,-np.inf,1])
# print(np.isinf(num))

# num=np.array([7,6,5,np.nan])
# print(np.nan_to_num(num,nan=4))

# num1=np.nan_to_num(num,posinf=100,neginf=123)
# print(num1)
