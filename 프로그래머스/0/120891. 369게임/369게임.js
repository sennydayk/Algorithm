function solution(order) {
  let count = 0;
  let arr = String(order).split('');
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] === "3" || arr[i] === "6" || arr[i] === "9") {
      count++
    }
  }
  return count;
}