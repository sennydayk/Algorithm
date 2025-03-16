// DFS로 풀기
// 외부 반복문 - numbers 배열 길이만큼 반복
// 내부 반복문 - 노드 배열 길이만큼 반복
// 내부 반복문에서 해당 노드 -number, +number 값을 각각 노드 배열에 다시 저장
// 모든 반복을 마친 노드 배열에서 target 값만 필터링

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