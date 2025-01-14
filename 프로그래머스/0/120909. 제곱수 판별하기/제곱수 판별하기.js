function solution(n) {
    // Math.sqrt는 소수점의 제곱수까지도 판별하므로 1로 나눈 나머지가 0인 것만이 정수
    if(Math.sqrt(n) % 1 === 0){
        return 1;
    }
    return 2;
}