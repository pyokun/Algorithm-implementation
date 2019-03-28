'''This program is for implement a LSH algorithm. Suppose we have three columns,
a={a,b,c,d}   b={a,b,e,f}  c={a,b,c,f}, how to find which is most relevent columns for d={a,c,f,e}.
'''
import numpy as np


a=['a','b','c','d']
b=['a','b','e','f']
c=['a','b','c','f']
d=['a','c','f','e']

#get union set of all columns
def get_union_set(a,b,c,d):
	return (set(a)|set(b)|set(c)|set(d))

union_set=get_union_set(a,b,c,d)

#convert a column to matrix
def convert_to_matrix(union_set,a):
	a_matrix=[0]*len(union_set)
	for i in range(len(union_set)):
		if list(union_set)[i] in a:
			a_matrix[i]=1
	return a_matrix

a_matrix=convert_to_matrix(union_set,a)
b_matrix=convert_to_matrix(union_set,b)
c_matrix=convert_to_matrix(union_set,c)
d_matrix=convert_to_matrix(union_set,d)
print(a_matrix,b_matrix,c_matrix,d_matrix)


#define several hash function
hash_1=[1,1]
hash_2=[5,1]
hash_3=[7,2]

#count the ans of minhash
def minhash(a_matrix,hash_1):
	minhash_ans=1000000
	mod=len(a_matrix)
	w,bias=hash_1
	for i in range(len(a_matrix)):
		if a_matrix[i]!=0:
			temp=(w*i+bias)%mod
			if temp<minhash_ans:
				minhash_ans=temp
	return minhash_ans

#get signature matrix.
hash_list=[hash_1,hash_2,hash_3]
matrix_list=[a_matrix,b_matrix,c_matrix,d_matrix]
def get_signature_matrix(matrix_list,hash_list):
	ans_matrix=1000*np.ones((len(hash_list),len(matrix_list)))
	for i in range(len(matrix_list)):
		for j in range(len(hash_list)):
			ans_matrix[j,i]=minhash(matrix_list[i],hash_list[j])
	return ans_matrix
ans_matrix=get_signature_matrix(matrix_list,hash_list)




def banding_tech(b,ans_matrix):
	band=[]
	while len(ans_matrix.T)>b:
		band.append(ans_matrix[:,:b])
		ans_matrix=ans_matrix[:,b:]
	return band

band=banding_tech(1,ans_matrix)
print(band)




