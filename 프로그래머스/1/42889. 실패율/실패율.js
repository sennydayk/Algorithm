// N = 전체 스테이지 개수, stages = 멈춰 있는 스테이지 번호(1~N+1)
// 실패율 = 해당 번호에 멈춰 있는 사용자 수 / 해당 스테이지를 클리어한 사용자 수

function solution(N, stages) {
    const stageInfo = [];
    
    stages.sort((a, b) => a - b); // 스테이지 번호순으로 정렬

    for (let stage = 1; stage <= N; stage++) {
        // 해당 스테이지에 멈춰있는 플레이어 수
        let failCount = 0;
        for (let j = 0; j < stages.length; j++) {
            if (stages[j] === stage) {
                failCount += 1;
            }
        }
        
        // 해당 스테이지에 도달한 플레이어 수
        let totalCount = 0;
        for (let j = 0; j < stages.length; j++) {
            if (stages[j] >= stage) {
                totalCount += 1;
            }
        }
        
        // 실패율 계산
        const failureRate = totalCount === 0 ? 0 : failCount / totalCount;
        
        // 스테이지 번호와 실패율 저장
        stageInfo.push({ stage, failureRate });
    }
    
    // 실패율 내림차순으로 정렬, 실패율이 같으면 스테이지 번호 오름차순
    stageInfo.sort((a, b) => {
        if (a.failureRate !== b.failureRate) {
            return b.failureRate - a.failureRate;
        }
        return a.stage - b.stage;
    });
    
    // 정렬된 스테이지 번호만 반환
    return stageInfo.map(info => info.stage);
}