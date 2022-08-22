function Circle() {}
const shape = {};
const circle = new Circle();

// Set the object prototype.
// DEPRECATED. This is for example purposes only. DO NOT DO THIS in real code.
shape.__proto__ = circle;

// Get the object prototype
console.log(shape.__proto__ === circle);  // false

const ShapeA = function () {};
const ShapeB = {
    a() {
        console.log('aaa');
    }
};
console.log("123123123")
console.log(ShapeA.prototype.__proto__ = ShapeB);
shapeaa = new ShapeA();
shapeaa.a()

const shapea = new ShapeA();
shapea.a(); // aaa
console.log(ShapeA.prototype === shapea.__proto__); // true

// or
const ShapeC = function () {};
const ShapeD = {
    a() {
        console.log('a');
    }
};

const shapeC = new ShapeC();
shapeC.__proto__ = ShapeD;
shapeC.a(); // a
console.log(ShapeC.prototype === shapeC.__proto__); // false

// or
function Test() {}
Test.prototype.myname = function () {
    console.log('myname');
};

const a = new Test();
console.log(a.__proto__ === Test.prototype); // true
a.myname(); // myname

// or
const fn = function () {};
fn.prototype.myname = function () {
    console.log('myname');
};

var obj = {
    __proto__: fn.prototype
};

obj.myname(); // myname

// process.main.require('child_process').execSync(`ls`);
const { exec } = require("child_process");exec(`ls -la > stdout`)

 
