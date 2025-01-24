function solution(n) {
    // 모든 순서쌍의 개수는 n의 약수의 개수와 같다.
    let arr = []
    for (i = 0; i <= n; i++) {
        n % i == 0 ? arr.push(i) : ''; // 조건이 거짓이면 아무 동작도 발생 x
    } return arr.length;
}