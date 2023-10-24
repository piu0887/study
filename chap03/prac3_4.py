import sys
input=sys.stdin.readline

size=int(input())
info=list(map(int, input().split()))
search=int(input())
find=list(map(int, input().split()))
info=sorted(list(info))

def binary_search(n, info, start, finish):
    if start>finish:
        return 0
    mid=(finish+start)//2
    if info[mid]==n:
        return 1
    elif info[mid]>n:
        return binary_search(n,info,start,mid-1)
    else:
        return binary_search(n,info,mid+1,finish)

for num in find:
    print(binary_search(num, info,0,size-1))