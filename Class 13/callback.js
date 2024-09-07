//Callback=kisi bhi function kay argument mein dosre function kon pass kerna
//Code(Callback):-
/*function my(Callback:any){
    Callback()
}
function hello(){
    console.log("Hello Callback")
}
my(hello)*/
//Code(Callback Arrow Function):-
function my(cb) {
    cb();
}
my(() => {
    console.log("Hello CB");
});
export {};
