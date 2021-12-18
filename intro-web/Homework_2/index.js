// querySelector using the same values for selection as css.
// const queryDiv = document.querySelector('div')
// const queryDivAll = document.querySelectorAll('div')
//create HTML elements

// ------------- Begin Homework 2 -------------

const manDOM = document.createElement('div')
manDOM.className = 'divH'
manDOM.innerHTML = '<h1>Manipulating the  DOM</h1>'
document.querySelector('main').append(manDOM)

const dyna = document.createElement('div')
dyna.className = 'divH'
dyna.innerHTML = '<h2>Dynamically!!</h2>'
document.querySelector('main').append(dyna)

const intro = document.createElement('div')
intro.className = 'divP'
intro.innerHTML = '<p>Welcome to Javascript!</p>'
document.querySelector('main').append(intro)

const work = document.createElement('div')
work.className = 'divP'
work.innerHTML = '<p>It does all the Work.</p>'
document.querySelector('main').append(work)

const colorPick = document.createElement('h1')
colorPick.innerHTML = 'Show a Color Picker'
document.querySelector('main').append(colorPick)

const favColor = document.createElement('label')
favColor.setAttribute('for', 'favcolor')
favColor.innerHTML = 'Select your favorite color:'
const colors = document.createElement('input')
colors.type = 'color'
colors.id = 'favcolor'
colors.name = 'favcolor'
colors.value = '#ff0000'
document.querySelector('main').append(favColor, colors)

document.querySelector('p').id = 'introMsg'

const queryDiv = document.querySelector('div')

// -------------- End Homework 2 --------------

const btnDiv = document.createElement('div')
btnDiv.id = 'btnDiv'
// document.querySelector('main').lastElementChild.append(btnDiv)
// document.querySelector('#root').append(btnDiv)
document.querySelector('main').append(btnDiv)
// const dynamicBtn = document.querySelector('h2')
// dynamicBtn.id="dynamicBtn"

queryDiv.style.backgroundColor = 'red'
const blueBtn = document.createElement('button')
const cyanBtn = document.createElement('button')
blueBtn.innerHTML = "Blue!"
cyanBtn.innerHTML = "Cyan!"
blueBtn.className = "colorBtn"
cyanBtn.className = "colorBtn"
// dynamicBtn.append(blueBtn)

// Functions do work immediately (IIF(E) -> Immediately Invoked Function Expression) or when asked.

// function theFunctionName(parameter) {
//    code goes here
// }

// function changeBackgroundBlue() {
//     console.log("Blue")
//     queryDiv.style.backgroundColor = 'blue'
    
// }
// function changeBackgroundCyan() {
//     console.log("Cyan");
//     queryDiv.style.backgroundColor = 'cyan'
// }
// blueBtn.onclick=changeBackgroundBlue()
// cyanBtn.onclick=changeBackgroundCyan

// function changeBackground(param) {
//     console.log("param: ", param);
//     queryDiv.style.backgroundColor = param
// }

// new way to write functions, function expression, aka fat arrow ( => ) functions
const changeBackground = (param) => {
    console.log("param: ", param);
    queryDiv.style.backgroundColor = param
}

 blueBtn.onclick = function() {changeBackground("blue")}
 cyanBtn.onclick = () => changeBackground("cyan")

 //create a form using JS
//  const colorForm = document.createElement('form')


const colorBtn = document.createElement('button')
colorBtn.innerHTML = "Change Color"
colorBtn.className = "colorBtn"
colorBtn.onclick = () => changeBackground(document.querySelector('input').value)


btnDiv.append(blueBtn, cyanBtn, colorBtn)