type obj = {
    name:string,
    age:number
}
type obj1 = {
    rollno:number,
    class:string
}
type r = obj & obj1

let boy : r = {
    name:"Muhammad Ibrahim Mubashir",
    age:13,
    rollno:14,
    class:"8th"
}
console.log(boy)