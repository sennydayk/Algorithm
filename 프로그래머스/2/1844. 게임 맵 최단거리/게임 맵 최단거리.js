// n*m 크기의 맵, 0=벽, 1=길
// (1,1)에서 (n,m)으로 가는 최단거리 구하기 (갈 수 없으면 -1)
// BFS로 풀기

function solution(maps) {
    const n = maps[0].length; // 가로의 길이 (열의 개수)
    const m = maps.length; // 세로의 길이 (행의 개수)
    
    // 이동 방향
    let directions = [
        [0, 1],
        [0, -1],
        [1, 0],
        [-1, 0]
    ];
    
    const queue = [[0, 0, 1]] // 현재 위치와 거리
    
    while (queue.length > 0) {
        const [x, y, distance] = queue.shift();
        
        if (x === m-1 && y === n-1) return distance;
        
        for (let [dx, dy] of directions) {
            let newX = x + dx;
            let newY = y + dy;
            // 좌표가 범위 내에 있고 1인 경우
            if (newX >= 0 && newX < m && newY >= 0 && newY < n && maps[newX][newY] === 1) {
                // 새로운 좌표와 +1된 거리를 저장
                queue.push([newX, newY, distance + 1]);
                // 중복 방지
                maps[newX][newY] = 0;
            }
        }
    }
    return -1;
}