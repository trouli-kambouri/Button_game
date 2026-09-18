
// INSERTING HTML ELEMENTS

// DEFINING VARIABLES

let i = 0; // number of button clicks

let s = i * 0.1 // seconds // It takes 100 milliseconds to click a button. (I googled it and confirmed by timing my button clicks on average).

let m = s / 60 // minutes

let h = m / 60 // hours

let d = h / 24 // days

let w = d / 7 // weeks

let y = d / 365 // years

let mm = y * 12 // months


// CLICK BUTTON FUNCTION

function clickButton()
{
    i++;
    document.getElementById("i").textContent = i;
}

// DATE LOG

new Date(year,month,day,hours,minutes,seconds,ms)
{
    return "button clicked on + ";
}