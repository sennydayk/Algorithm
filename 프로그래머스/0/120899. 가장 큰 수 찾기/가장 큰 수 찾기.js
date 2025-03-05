function solution(array) {
    var answer = [];
    var maxNum = Math.max(...array);
    answer.push(maxNum);
    answer.push(array.indexOf(maxNum));
    return answer;
}