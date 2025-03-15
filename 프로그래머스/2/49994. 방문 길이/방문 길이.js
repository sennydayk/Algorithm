// 좌표를 벗어나는지 체크하는 함수
function isValidMove(nx, ny) {
    return nx <= 5 && nx >= -5 && ny <= 5 && ny >= -5;
}

// 명령어를 받아 다음 좌표를 반환하는 함수
function updateLocation(x, y, dir) {
    switch (dir) {
        case "U":
            return [x, y + 1];
        case "D":
            return [x, y - 1];
        case "R":
            return [x + 1, y];
        case "L":
            return [x - 1, y];
    }
}

function solution(dirs) {
    let x = 0;
    let y = 0;
    
    // 중복 제거를 위해 집합으로 선언
    const visited = new Set();
    
    // 주어진 명령어대로 움직이면서 좌표 저장
    for (const dir of dirs) {
        const [nx, ny] = updateLocation(x, y, dir);
        
        // 좌표평면을 벗어난 좌표는 저장하지 않음
        if (!isValidMove(nx, ny)) {
            continue;
        }
        
        // 중복 체크를 정확하게 하기 위해 객체 대신 문자열로 저장
        visited.add(`${x}${y}${nx}${ny}`);
        visited.add(`${nx}${ny}${x}${y}`);
        
        // 다음 좌표로 이동
        [x, y] = [nx, ny];
    }
    
    // A->B, B->A 경로 모두 저장했으므로 2로 나눠줌
    return visited.size / 2;
}