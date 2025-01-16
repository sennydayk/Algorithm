function solution(array) {
    // js 배열에 sort()를 하면 정수가 아닌 문자 기준으로 정렬된다.
    array.sort((a, b) => b - a)
    return array[Math.trunc(array.length / 2)]
}