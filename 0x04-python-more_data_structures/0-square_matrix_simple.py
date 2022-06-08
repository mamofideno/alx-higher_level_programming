#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    mat2=[]
    for i in matrix:
        temp=[]
        for j in i:
            temp.append(j*j)
        mat2.append(temp)
    return (mat2)
