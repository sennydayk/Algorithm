// a, b가 같아질 때까지 반복
// a, b는 각각 다음에 2로 나눈 값을 올림한 값으로 다시 부여받게 됨

function solution(n,a,b) {
    let count = 0;
    while (a != b) {
        a = Math.ceil(a / 2);
        b = Math.ceil(b / 2);
        count += 1;
    }
    return count;
}