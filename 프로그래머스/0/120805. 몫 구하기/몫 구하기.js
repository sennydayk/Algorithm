function solution(num1, num2) {
    return ~~(num1 / num2)
}

// ~ 연산자
// ~n -> -(n+1) 반환
// ex. n = 5  ~n = -6  ~~n = 5
// 따라서 ~~을 붙이면 소수점 아래를 버림한 정수값을 반환할 수 있음