# A[] repesent coefficient of first polynomial
# B[] repesent coefficient of Second polynomial
 
def add(A,B,m,n):
  size = max(m,n)
  C=[ 0 for i in range(size)]
  
  for i in range(0,m,1):
      # each term from first polynomial
      C[i]=A[i]
      #Add each term of second poly add it to c
     
  for i in range(n):
      C[i]+=B[i]
      
      return C 

#A function point a poly

def display(poly,n):
    for i in range(n):
        print(poly[i],end="")
        
        if(i!=0):
            print("X ^ ",i,end="")
        if(i!=n-1):
            print(" + ",end="")
       #driver code      
if__name__='__main__'
    
A=[1,2,3,4]
B=[0,7,0,5]
m=len(A)
n=len(B)

print("\n first polynomial is :")
display(A,m)

print("\n Second polynomial is :")
display(B,n)

C=add(A,B,m,n)
size=max(m,n)

print("\n Addition of polynomial :")
display(C,size)   



















                
       