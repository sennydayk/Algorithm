function solution(n, k) {
    var answer = 0;
    if (n >= 10) {
        var dc = 0;
        dc = ~~(n/10) * 2000
        answer = 12000 * n + 2000 * k - dc
    } else {
        answer = 12000 * n + 2000 * k
    }
    return answer;
}