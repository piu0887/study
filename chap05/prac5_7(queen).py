pos = [0] * 8
flag_a = [False] * 8   # 각 행에 퀸을 배치했는지 체크
flag_b = [False] * 15   # 오른쪽 대각선에 퀸을 배치했는지 체크
flag_c = [False] * 15   # 왼쪽 대각선에 퀸을 배치했는지 체크

def put () -> None:

    for j in range(8) :
        for i in range(8):
            print('◼︎' if pos[i] == j else '◻︎', end='')
        print()
    print()
    

def set(i: int) -> None:

    for j in range(8) :
        if(     not flag_a[j]                  # j행에 퀸을 배치하지 않았다면
            and not flag_b[i +j]               # 오른쪽 대각선 배치하지 않았다면
            and not flag_c[i-j+7]):            # 왼쪽 대각선에 퀸을 배치하지 않았다면
            pos[i] = j
            if i == 7 :
                put()
            else :
                flag_a[j] = flag_b[i+j] = flag_c[i-j+7] = True
                set(i+1)            # 다음열에 퀸을 배치
                flag_a[j] = flag_b[i+j] = flag_c[i-j+7] = False

set(0)