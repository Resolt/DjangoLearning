var newCSS = {
	'color': 'white',
	'background': 'blue',
	'border': '10px solid black'
}
$('h1').css(newCSS)

$('h1').click(function () {
	console.log("Clicked!")
})