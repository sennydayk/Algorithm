// DFS로 풀기
// 루트 노드는 0, 각 노드의 왼쪽 자식은 -인접한 요소, 오른쪽 자식은 +인접한 요소
// numbers 배열에 요소가 존재하는 동안 반복
// 인접한 요소가 있으면 계속 -인접요소 연산, 없으면 +인접요소 연산
// 최종 결과값이 target이면 count 1 증가

function solution(numbers, target) {
    let nodes = [0];
    
    for (let i=0; i < numbers.length; i++) {
        const number = numbers[i];
        const nextNodes = [];
        
        for (let node of nodes) {
            nextNodes.push(node - number);
            nextNodes.push(node + number);
        }
        
        nodes = nextNodes;
    }
    const result = nodes.filter((v) => v === target);
    return result.length;
}