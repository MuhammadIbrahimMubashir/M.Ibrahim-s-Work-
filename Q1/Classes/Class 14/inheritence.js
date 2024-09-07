/*//Code(Inheritence):-
//Base Class Or Parent Class
class Product{
    name:any
    price:any
    constructor(n:string,p:number){
        this.name = n
        this.price = p
    }
    disply(){
        console.log(`LED ${this.name}'s And Price Is ${this.price}PKR`)
    }
}
//Child Class Or Derived Class
class Electronic extends Product{
    warranty:any
    constructor(n:string,p:number,w:number){
        super(n,p)
        this.warranty = w
    }
    showwarranty(){
        super.disply(){
            console.log(`It's Warranty Is ${this.warranty} Years`)
        }
    }
}
let led = new Electronic("Samsung",100000,5)
led.showwarranty()*/
//Code(Inheritence Product)
class Product {
    name;
    price;
    constructor(n, p) {
        this.name = n;
        this.price = p;
    }
    disply() {
        console.log(`${this.name} And It's Price Is ${this.price}PKR`);
    }
}
let Laptop = new Product("Dell Laptop", 10000);
Laptop.disply();
let mobile = new Product("IPhone 15 Pro Max", 500000);
mobile.disply();
export {};
