let $ = document

let btn = $.getElementById("buuton-send")
let resualtTextArea = $.getElementById("resu")
let index = 1
let telephoneNumber = ''
let number = ''
$.querySelector(".form").addEventListener("submit", function(e) { e.preventDefault() })


btn.addEventListener("click", (ev) => {
    telephoneNumber = $.getElementById("tele")
    number = $.getElementById("number")
    ev.preventDefault()
    resualtTextArea.value = ""

    index = 1
    if (!telephoneNumber.value.trim() && !number.value.trim()) {
        alert("Invalid info")
    } else if (number.value < 1) {
        number.value = ''
        alert("Invalid Number")
    } else if (telephoneNumber.value.trim().length != 11 || isNaN(telephoneNumber.value) || isNaN(number.value)) {
        alert("Invalid telephone")
    } else {
        eel.getinfo(telephoneNumber.value, number.value)
        resualtTextArea.value = `send sms to : ${telephoneNumber.value} \nNumber : ${number.value} \n${"-------------------------------------------------"}`
        ev.target.setAttribute("disabled", "true")
        telephoneNumber.setAttribute("disabled", "true")
        number.setAttribute("disabled", "true")
        telephoneNumber.style.cssText = "opacity:0.3"
        number.style.cssText = "opacity:0.3"
        ev.target.style.cssText = "opacity:0.3"
    }
})

eel.expose(activebutton);

function activebutton() {
    btn.removeAttribute("disabled")
    telephoneNumber.removeAttribute("disabled")
    number.removeAttribute("disabled")
    telephoneNumber.style.cssText = "opacity:1"
    number.style.cssText = "opacity:1"
    btn.style.cssText = "opacity:1"
}

eel.expose(getResualt);

function getResualt(resualt) {
    resualtTextArea.value += `\n[${index}] => ${resualt}\n----------------------------------------`
    index++
}