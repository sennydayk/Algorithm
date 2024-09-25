# 종료조건 전까지 계속해서 입력받기
while True :
    a = input()
    stack = []
    
    # 사용자가 . 입력 시 종료
    if a == "." :
        break
    
    # 왼쪽 괄호가 입력되면 stack에 추가
    for i in a :
        if i == '[' or i == '(' :
            stack.append(i)
        
        elif i == ']' :
            # [] 맞으면 제거해서 stack 비우기
            if len(stack) != 0 and stack[-1] == '[' :
                stack.pop()
            else : 
                stack.append(']')
                break
        elif i == ')' :
            # () 맞으면 제거해서 stack 비우기
            if len(stack) != 0 and stack[-1] == '(' :
                stack.pop()
            else :
                stack.append(')')
                break
    
    # 결과값 출력
    if len(stack) == 0 :
        print('yes')
    else :
        print('no')