function solution(sides) {
  let a = Math.max(...sides)
    let b = sides.reduce((acc,cur,i)=>{
        return acc + cur 
    },0) 
    let c = b - a
    
    if(a < c){
        return 1
    }
    return 2;
}