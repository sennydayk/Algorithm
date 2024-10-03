# 입력
# 첫째 줄 : 테스트 케이스 T
# 각 케이스 첫째 줄 : 공백
# 각 케이스 둘째 줄 : 세준과 세비의 병사 수 N, M
# 각 케이스 셋째 줄 : 세준 병사의 힘
# 각 케이스 넷째 줄 : 세비 병사의 힘

# 출력
# 세준이가 이기면 S, 세비가 이기면 B, 둘 다 아니면 C

# 해결 방안
# 세준, 세비 병사의 힘을 정렬한 후 가장 앞의 값을 비교

T = int(input())

for _ in range(T):
    # 공백 출력
    input()
    # 입력값 받기
    N, M = map(int, input().split())
    sejun = list(map(int, input().split()))
    sebi = list(map(int, input().split()))

    # 세준, 세비 힘 리스트 오름차순 정렬
    sejun.sort()
    sebi.sort()

    # 세준, 세비 병사가 한 명 이상씩 있을 경우 반복
    while sejun and sebi:
        # 가장 약한 세준 병사의 힘이 가장 약한 세비 병사의 힘보다 크거나 같을 때
        if sejun[0] >= sebi[0]:
            # 세비 병사가 죽음
            sebi.pop(0)
        # 반대의 경우
        elif sejun[0] < sebi[0]:
            # 세준 병사가 죽음
            sejun.pop(0)
    
    # 결과 출력
    if sejun:
        print('S')
    elif sebi:
        print('B')
    else:
        print('C')