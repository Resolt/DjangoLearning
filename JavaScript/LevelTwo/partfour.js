var names = []

if (prompt("Would you like to start the app? y/n") === "y") {
	var cmd = ""
	while (cmd !== "quit") {
		cmd = prompt("What would you like to do? (add, remove, display, quit)")
		if (cmd === "quit" || cmd === null) {
			break
		} else if (cmd === "add") {
			var name = prompt("Please enter name to add")
			addName(name)
		} else if (cmd === "remove") {
			var name = prompt("Please enter name to remove")
			removeName(name)
		} else if (cmd === "display") {
			displayNames()
		} else {
			console.log("Unknown action: " + cmd)
		}
	}
}

function displayNames() {
	for (name of names) {
		console.log(name)
	}
}

function removeName(name) {
	var i = names.indexOf(name)
	if (i !== -1) {
		names.splice(names.indexOf(name), 1)
	} else {
		console.log(name + " is not in names")
	}
}

function addName(name) {
	if (names.indexOf(name) === -1) {
		names.push(name)
	} else {
		console.log(name + " is already in the names")
	}
}