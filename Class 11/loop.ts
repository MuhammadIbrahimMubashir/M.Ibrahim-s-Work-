//syntax for(){}
//for(let i = 0;i <= 10,i++)
//        |        |     |
//  variable  condition  increment/decrement

//Code(loop):-
/*for(let i = 0; i <= 10; i++){
    console.log(i)
}*/

//Code(loop to add):-
let sum = 0
for(let i = 0; i <= 10; i++){
    sum += i;
}
console.log("Sum of first 10 numbers is:",sum)