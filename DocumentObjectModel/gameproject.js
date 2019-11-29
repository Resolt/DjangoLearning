var btn = document.querySelector("#b")
var fields = document.querySelectorAll("td")

function clearBoard() {
	for (field of fields) {
		field.textContent = ""
	}
}

btn.addEventListener("click", clearBoard)

turn = "X"

function turnUpdate() {
	if (turn === "X") {
		turn = "O"
	} else {
		turn = "X"
	}
}

function fieldClick() {
	if (this.textContent === "") {
		this.textContent = turn;
		turnUpdate()
	}
}
for (field of fields) {
	field.addEventListener("click", fieldClick)
}