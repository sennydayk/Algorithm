function solution(s1, s2) {
    return s1.filter(v => s2.includes(v)).length;
    
    // 교집합으로 풀기
    // return s1.length + s2.length - new Set([...s1, ...s2]).size
}