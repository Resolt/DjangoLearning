var lbs = prompt("Give me the pounds");

var lbkgr = 0.454;
var kgs = parseFloat(lbs) * lbkgr;
kgs = Math.round(kgs)

alert("These are the KGs: " + String(kgs))

console.log("Conversion Completed")