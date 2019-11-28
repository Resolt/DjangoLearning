// var hot = false
// var temp = parseInt(prompt("What is the temperature?"))
var temp = NaN
while (isNaN(temp)) {
	temp = parseInt(prompt("What is the temperature?"))
}

var msg = null

if (temp >= 80) {
	msg = "It's sooo hot"
} else if (temp >= 50) {
	msg = "It's average temp today"
} else if (temp >= 32) {
	msg = "It's pretty cold out"
} else {
	msg = "It's freeeezing"
}

console.log(temp)
console.log(msg)
alert(msg)