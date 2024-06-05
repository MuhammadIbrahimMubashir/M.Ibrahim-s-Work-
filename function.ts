export function mycal(n1:number,n2:number,sign:string){
    if(sign == "Addition"){
        console.log(n1 + n2)
    }
    else if(sign == "Subtraction"){
        console.log(n1 - n2)
    }
    else if(sign == "Multiplication"){
        console.log(n1 * n2)
    }
    else if(sign == "Division"){
        console.log(n1 / n2)
    }
    else{
        console.log("Invaild Sign")
    }
}