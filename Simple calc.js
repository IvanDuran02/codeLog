// receive operation
var operation = prompt("what operation would you like to use?\n[addition]-[subtraction]-[multiplication]-[division]")
// prompt user for 1st number
var num1 = parseFloat(prompt("what number would you like to " + operation))
// prompt user for 2nd number
var num2 = parseFloat(prompt("and whats the 2nd number you would like to " + operation))
// make sure operation received is valid
if (operation.toLowerCase() === "addition") {
// if addition was selected add and print.
  var answer = num1 + num2
  console.log(answer)
// if operstion subtraction is selected.
} else if (operation.toLowerCase() === "subtraction") {
  var answer = num1 - num2
  console.log(answer)
// if operation multiplication is selected.
} else if (operation.toLowerCase() === "multiplication") {
  var answer = num1 * num2
  console.log(answer)
// if operation division is selected.
} else if (operation.toLowerCase() === "division") {
  var answer = num1 / num2
  console.log(answer)
// print if nothing is true
} else {
  console.log("the operation was invalid.")
}
