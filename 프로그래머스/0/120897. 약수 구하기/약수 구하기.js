function solution(n) {
    let result = []
    for (i = 0; i <= n; i++) {
        if (n % i == 0) {
            result.push(i);
        }
    } return result;
}