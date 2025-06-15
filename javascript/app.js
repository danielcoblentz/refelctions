// defining vars
let varName = 14;
let person = "Daniel";

// printing to terminal
console.log("hello there");
console.log("hello there" + person);

// conditiona lstatements
if (varName > 6) {
    console.log("yup more than 6!")
}
else{
    console.log("nope!")
}

//loops: has to use let
for (let i = 0; i < 5; i ++){
    console.log(i)
}


// functions
function sayHello(person) {
    console.log(person + "!")
}
sayHello("daniel")  


//arrays
let colors = ["green", "red", "black"];
for (let i = 0; i < colors.length; i ++){
    console.log(colors[i]);
}

//printing a specific element
console.log(colors[2]);

const myset = new Set();
myset.add(1);
console.log(myset);