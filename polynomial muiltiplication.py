# A[] repesent coefficient of first polynomial
# B[] repesent coefficient of Second polynomial

def mul(A,B,m,n):
 C =[0]* (m+n-1)
 for i in range(0, m, 1):
 #multiplying by current term of first polynomial
 #to each term of second polynomial
  for j in range(n):
   C[i+j] += A[i]*B[j]
 return C

def display(poly,n):
    for i in range(n):
        print(poly[i],end="")
        if(i!=0):
            print("X^",i,end="")
        if(i!=n-1):
               print(" + ",end="") 
                
               
if __name__== '__main__':
 A=[1,1,2,3]
    
B=[0,7,0,5]
m=len(A)
n=len(B)

print("\n First polynomial is :")
display(A,m)

print("\nSecond polynomial is :")
display(B,n)

C=mul(A,B,m,n)

print("\n Multiplication of polynomial is :")
display(C,m+n-1)
                   