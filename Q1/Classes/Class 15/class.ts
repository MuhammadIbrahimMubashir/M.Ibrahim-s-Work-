//Code(Class Private):-
/*class Person{
    private_name:string ="lal"
    getname(){
        return this.private_name="Lal"
    }
}
let  p1:Person = new Person()
console.log(p1.getname())
console.log(p1 instanceof Person)*/

//Code(Class Protected):-
/*class Person {
    protected_name:any ="Lal"
    age = 30
}
class Human extends Person{
    getname(){
        return this.protected_name="Lal Bhai"
    }
}
let h1 = new Human()
console.log(h1.protected_name)
console.log(h1.getname)*/

//Code(OverRight):-
class Person{
    name = "Ratan Lal"
    age = 30
}
class Human extends Person{
    name: string="Lal"
}
let h1 = new Human()
console.log(h1.name)