function solution(my_string) {
    const arr = my_string.replaceAll(/[A-z]/g, "").split("");
    return arr.reduce((a, c) => a + Number(c), 0);
}