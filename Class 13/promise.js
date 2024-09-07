//Code(Promise):-
/*let mypromise = new Promise ((resolve,reject) => {
    console.log("Pending")
    setTimeout(() => {
        console.log("Resolve")
        resolve("Muhammad Ibrahim Mubashir")
    },3000);
})
mypromise.then((res) => {console.log(res)})*/
//Code(Promise):-
/*let mypromise = new Promise ((resolve,reject) => {
    console.log("Pending")
    setTimeout(() => {
        console.log("Reject")
        reject(new Error("Nahi"))
    },3000);
})
mypromise.then((res) => {console.log(res)})
.catch((err) => console.log(err))*/
//Code(Promise Small):-
/*let url = 'https://jsonplaceholder.typicode.com/todos/1'
let fetchData:any = fetch(url)
.then((res:any) => res.json())
.then((res:any) => {console.log(res)})
.catch((err:any)=> {console.log(err)})*/
//Code(Promise Try Catch):-
async function mypromise() {
    try {
        let url = 'https://jsonplaceholder.typicode.com/todos/1';
        let fetchData = fetch(url)
            .then((res) => res.json())
            .then((res) => { console.log(res); });
    }
    catch (error) {
        ((err) => { console.log("Find An Error"); });
    }
}
mypromise();
export {};
