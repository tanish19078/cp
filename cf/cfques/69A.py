n=int(input())
mat=[]
for i in range(n):
    mat.append(list(map(int,input().split())))
tr=[[mat[j][i] for j in range(n)]for i in range(3)]
rs=[sum(tr[i])for i in range(3)]
if rs[0]==rs[1]==rs[2]==0:
    print("YES")
else:
    print("NO")