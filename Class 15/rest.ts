//Code(Res):-
function abc(a:number,b:number,c:number,...rest: number[]){
    console.log("Rest:",rest)
    return a+b+c
}
console.log(abc(1,2,3,4,5,6,7,8,9,10))