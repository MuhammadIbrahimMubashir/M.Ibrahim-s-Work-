import inquirer from 'inquirer';
import { mycal } from './function.js';
let answer = await inquirer.prompt([
    {
        type: "number",
        message: "Enter Your First Number:",
        name: "n1",
    },
    {
        type: "number",
        message: "Enter Your Second Number:",
        name: "n2",
    },
    {
        type: "list",
        message: "Select Your Operation:",
        name: "sign",
        choices: ["Addition", "Subtraction", "Multiplication", "Division"]
    }
]);
mycal(answer.n1, answer.n2, answer.sign);
