import numpy as np

'''
Calculați numărul liniilor unei matrice cu proprietatea că au elementele în ordine
crescătoare
'''
def nrLinii(matrix):
    count=0
    for i in range(matrix.shape[0]):
        bool='true'
        for j in range(1,matrix.shape[1]):
            if(matrix[i,j]<matrix[i,j-1]):
                bool='false'
                break
        if(bool=='true'):
            count+=1
    return count

''' Determinați coloanele unei matrice cu proprietatea că au cel mai mic element egal cu 5.'''
def detCol(matrix):
    listaCol=[]
    for j in range(matrix.shape[1]):
        min=matrix[0,j]
        for i in range(matrix.shape[0]):
            if(matrix[i,j]<min):
                min=matrix[i,j]
        if(min==5):
            listaCol.append(j)
    print(listaCol)

'''Implementați algoritmul de sortare prin metoda bulelor pentru a ordona fiecare linie a unei
matrice'''
def sortareBLin(matrix):
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for k in range(j+1,matrix.shape[1]):
                if(matrix[i,k]<matrix[i,j]):
                    aux=matrix[i,k]
                    matrix[i,k]=matrix[i,j]
                    matrix[i,j]=aux


'''Implementați algoritmul de sortare prin inserție pentru a ordona fiecare coloană a unei
matrice'''
def sortareICol(matrix):
    for j in range(matrix.shape[1]):
        for i in range(1,matrix.shape[0]):
            key=matrix[i,j]
            k=i-1
            while k>=0 and key<matrix[k,j]:
                matrix[k+1,j]=matrix[k,j]
                k-=1
                matrix[k+1,j]=key
'''Fie A și B două matrice pătratice și n un număr natural nenul. Calculați 𝐴^𝑇, A+B, A*B și 𝐴^n.'''
def transpusa(matrix):
    for i in range(matrix.shape[0]):
        for j in range(i+1,matrix.shape[1]):
            matrix[i,j],matrix[j,i]=matrix[j,i],matrix[i,j]


def adunare(matrix1,matrix2):
    for i in range(matrix1.shape[0]):
        for j in range(matrix1.shape[1]):
            matrix1[i,j]=matrix1[i,j]+matrix2[i,j]

def inmultire(matrix1,matrix2):
    rezmatrix=np.dot(matrix1,matrix2)
    print(rezmatrix)

def putere(matrix,n):
    for i in range (1,n):
        matrix=np.dot(matrix,matrix)
    print(matrix)

def main():
    matrix=np.loadtxt('matrix.txt')
    print(nrLinii(matrix))
    detCol(matrix)
    sortareBLin(matrix)
    print (matrix)
    sortareICol(matrix)
    print(matrix)
    transpusa(matrix)
    print(matrix)
    matrix2=np.loadtxt('matrix2.txt')
    adunare(matrix2,matrix)
    print(matrix2)
    matrix3=np.loadtxt('matrix3.txt')
    matrix4=np.loadtxt('matrix4.txt')
    inmultire(matrix3,matrix4)
    putere(matrix4,1)

main()