MOVE_MESSAGE = "{} {}"
record = []

def move (N, start, destination):
    record.append(MOVE_MESSAGE.format(start, destination))

def hanoi (n, start, destination, via):

    #하노이 탑 규칙에 따라 원반을 옮기고, 옮길때 마다 원반의 시작 위치와 이동한 위치를 출력합니다.
    #마지막으로 총 이동 횟수를 반환합니다.
    #params
    # n: 총 원반 개수    start: 시작기둥   destination : 도착기둥   via: 보조 기둥 : return count:

    # 원반이 1개 일 때 시작 기둥에서 도착 기둥까지 한번에 이동
    if n <= 1:
        move ( 1, start, destination)
        return 1
    
    count = 0 
    # 원반이 n-1개를 시작 기둥에서 보조 기둥으로 이동

    count += hanoi (n-1, start, via, destination)

    # 가장 큰 원반을 시작 기둥에서 도착 기둥으로 이동 Move(1,start,detination)
    count +=1
    move(n,start, destination)

    #원반 n-1개를 보조기둥에서 도착기둥으로 이동
    count += hanoi(n-1,via,destination,start)

    return count

if __name__ == '__main__' :
    n= int(input())
    start = 1
    destination = 3
    via =2

    total_count = hanoi(n,start,destination,via)
    print(total_count)
    if len(record) <20 :
        for i in range(len(record)) :
            print(record[i])
        