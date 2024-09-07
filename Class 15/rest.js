//Code(Res):-
function abc(a, b, c, ...rest) {
    console.log("Rest:", rest);
    return a + b + c;
}
console.log(abc(1, 2, 3, 4, 5, 6, 7, 8, 9, 10));
export {};
