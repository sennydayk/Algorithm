function solution(num, k) {
   if(num.toString().indexOf(k)>-1){
      return num.toString().indexOf(k)+1
   } else {
      return -1
   }
}