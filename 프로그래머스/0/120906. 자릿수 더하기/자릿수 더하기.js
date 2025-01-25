function solution(n) {
     let answer = 0;
    let letters = n.toString();
    
    for(let i = 0; i < letters.length; i++) {
        answer += Number(letters[i]);
    }
    
    return answer;
}