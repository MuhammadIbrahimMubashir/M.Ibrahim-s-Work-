export function mycal(n1, n2, sign) {
    if (sign == "Addition") {
        console.log(n1 + n2);
    }
    else if (sign == "Subtraction") {
        console.log(n1 - n2);
    }
    else if (sign == "Multiplication") {
        console.log(n1 * n2);
    }
    else if (sign == "Division") {
        console.log(n1 / n2);
    }
    else {
        console.log("Invaild Sign");
    }
}
