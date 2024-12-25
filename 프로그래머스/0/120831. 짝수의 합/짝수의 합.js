function solution(n) {
    arr = Array(n).fill(0).map((_, i) => i+1)
    arr_even = arr.filter(v => v % 2 === 0)
    sum = arr_even.reduce((a, c) => a + c, 0)
    return sum;
}