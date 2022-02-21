console.log("Hello World!!!");
//
const yourName = prompt("Enter your name")
// const yourName = "Pavlo"

//
console.log(`Hello ${yourName}`);
//
function factorializer(num) {
    if (num < 0)
        return -1;
    else if (num == 0)
        return 1;
    else {
        return (num * factorializer(num - 1));
    }
}

console.log("Your name has " + yourName.length + " letters; " + yourName.length + "! = " + factorializer(yourName.length));
// 
let today = new Date();
let dd = String(today.getDate()).padStart(2, '0');
let mm = String(today.getMonth() + 1).padStart(2, '0');
let yyyy = today.getFullYear();
today = mm + '/' + dd + '/' + yyyy;
const dateOfBirthday = prompt(`Enter date of your birthday "01/01/2000" format`)
// const dateOfBirthday = "07/01/2001";
const birthday = new Date(dateOfBirthday);
const now = Date.now();
const diffTime = Math.abs(now - birthday);
const diffYears = Math.floor(diffTime / (1000 * 60 * 60 * 24 * 356));
const diffDays = Math.floor(diffTime / (1000 * 60 * 60 * 24));
console.log(`Today is ${today}, you are ${diffYears} years (${diffDays} days) old.`);
//