config = input("enter spatial or planar: ")
farr=[]
if config=="spatial":
    lamda = 6
elif config=="planar":
    lamda = 3
n = int(input("enter number of links:"))
joints = n

arr=[]
for i in range(n-1):
    tyj=int(input("enter 1 for revolute joint, 2 for prismatic, 3 for cylindrical, 4 for spherical:"))
    arr.append(tyj)





k=n-1
sum=0
for i in range(k):
    a = lamda-arr[i]
    sum = sum+a
df = lamda*(n-1)-sum

print("dof", df)







