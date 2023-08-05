#taking inputs
n=int(input())
ele=list(map(int,input().split()))
k=int(input())

#appending to the list
#print(ele)
templist=ele
for i in range(0,k):
    i_pop = ele[i]
    ele.append(i_pop)

pop_list=ele[k:]
for i in pop_list:
    print(i,end=" ")