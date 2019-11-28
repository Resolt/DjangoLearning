var firstName = prompt("What is your first name?")
var lastName = prompt("What is your last name?")
var age = parseInt(prompt("How old are you?"))
var height = parseInt(prompt("How tall are you in cm?"))
var petName = prompt("What is the name of your pet?")

var nameMatch = firstName[0] === lastName[0]
var ageMatch = age < 30 && age > 20
var heightMatch = height >= 170
var petMatch = petName[petName.length - 1] === "y"

if (nameMatch && ageMatch && heightMatch && petMatch) {
	console.log("You're my spy, guy")
}