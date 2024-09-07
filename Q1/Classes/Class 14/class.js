//Code(Class Easy):-
/*class Person{
    name ! : string
    age : any
}
let person = new Person()
person.name = "Muhammad Ibrahim Mubashir"
person.age = 13
console.log(person)*/
//Code(Class):-
/*class Human{
    name:any
    age:any
    constructor(n:string,a:number){
        this.name = n
        this.age = a
    }
}
let s1 = new Human ("Muhammad Ibrahim Mubashir",13)
let s2 = new Human ("Ali",50)
console.log(s1)
console.log(s2)*/
//Code(Class Rename):-
/*class Human{
    name : any
    constructor(n:string){
        this.name = n
    }
    rename(n:any){
        this.name = n
    }
}
let s1 = new Human ("Muhammad Ibrahim Mubashir")
console.log("Before",s1)
s1.rename("Ali")
console.log("After",s1)*/
//Code(Class Extends):-
class Student {
    name;
    rollnumber;
    constructor(n, r) {
        this.name = n;
        this.rollnumber = r;
    }
}
class Teacher extends Student {
    id;
    constructor(n, r, i) {
        super(n, r);
        this.id = i;
    }
}
let s1 = new Student("Muhammad Ibrahim Mubashir", 14);
let t1 = new Teacher("Ali", 30, 5);
console.log(s1);
console.log(t1);
export {};
