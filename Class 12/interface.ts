// interface(defined type previsly in object)
// Syntax = interface my{}

//Code(Interface):-
/*interface student {
    name:string,
    address:string
}
let Student:student = {
    name:"Waqar",
    address:"Defence Phase 8"
}
console.log(Student)*/

//Code(Interface Extends):-
interface std {
    name:string,
    rollno:number,
    phoneno:number,
    age:number
}
interface tec extends std {
    gmail:string
}

let s1:std = {
    name:"Ali",
    rollno:4,
    phoneno:38392432,
    age:14
}
console.log("Student",s1)

let t1:tec = {
    name:"Ahmed",
    rollno:19,
    phoneno:786448,
    age:34,
    gmail:"ahmed@gmail.com"
}
console.log("Teacher",t1)

//Stale Obj
s1 = t1