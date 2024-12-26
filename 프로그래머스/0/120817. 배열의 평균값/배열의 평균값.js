function solution(numbers) {
    sum = numbers.reduce((a, c) => a + c, 0)
    return sum / numbers.length;
}