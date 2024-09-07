// interface(defined type previsly in object)
// Syntax = interface my{}
let s1 = {
    name: "Ali",
    rollno: 4,
    phoneno: 38392432,
    age: 14
};
console.log("Student", s1);
let t1 = {
    name: "Ahmed",
    rollno: 19,
    phoneno: 786448,
    age: 34,
    gmail: "ahmed@gmail.com"
};
console.log("Teacher", t1);
//Stale Obj
s1 = t1;
export {};
