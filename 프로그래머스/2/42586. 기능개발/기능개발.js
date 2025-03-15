// 배포되는 날짜 = (100 - progress) / speed 를 올림한 값
// 배포되는 날짜를 담은 큐에서 첫 번째 요소가 다음 요소보다 작을 때까지 다음 요소를 제거

function solution(progresses, speeds) {
    const days = [];
    const result = [];
    
    for (let i=0; i < progresses.length; i++) {
        days.push(Math.ceil((100 - progresses[i]) / speeds[i]))
    }
    
    while(days.length > 0) {
        const firstDay = days[0]
        let count = 0;
        
        while (days.length > 0 && days[0] <= firstDay) {
            days.shift(); // 배포된 작업 제거
            count++;
        }
        result.push(count);
    } 
    return result;
}