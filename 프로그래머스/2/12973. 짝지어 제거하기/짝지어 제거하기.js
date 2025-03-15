// 스택을 만들고 문자열을 순회
// 해당 문자가 스택의 마지막 요소와 같은 문자면 pop, 아니면 push

function solution(s) {
    const stack = [];
    const s_arr = [...s];
    for (let i=0; i < s_arr.length; i++) {
        if (s_arr[i] === stack[stack.length - 1]) {
            stack.pop();
        } else stack.push(s_arr[i]);
    }
    if (stack.length === 0) {
        return 1;
    } else return 0;
}
