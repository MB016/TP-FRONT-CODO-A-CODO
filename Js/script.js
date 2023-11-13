const btnLeft = document.querySelector(".btn-left"),
      btnRight = document.querySelector(".btn-right"),
      slider = document.querySelector("#slider"),
      sliderSection = document.querySelectorAll(".slider-section");


btnLeft.addEventListener("click", e => moveToLeft())
btnRight.addEventListener("click", e => moveToRight())

setInterval(() => {
    moveToRight()
}, 3000);


let operacion = 0,
    counter = 0,
    widthImg = 100 / sliderSection.length;

function moveToRight() {
    if (counter >= sliderSection.length-1) {
        counter = 0;
        operacion = 0;
        slider.style.transform = `translate(-${operacion}%)`;
        slider.style.transition = "none";
        return;
    } 
    counter++;
    operacion = operacion + widthImg;
    slider.style.transform = `translate(-${operacion}%)`;
    slider.style.transition = "all ease .6s"
    
}  

function moveToLeft() {
    counter--;
    if (counter < 0 ) {
        counter = sliderSection.length-1;
        operacion = widthImg * (sliderSection.length-1)
        slider.style.transform = `translate(-${operacion}%)`;
        slider.style.transition = "none";
        return;
    } 
    operacion = operacion - widthImg;
    slider.style.transform = `translate(-${operacion}%)`;
    slider.style.transition = "all ease .6s"
    
    
}   


/* SLIDER 2*/

const btnLeft2 = document.querySelector(".btn-left2"),
      btnRight2 = document.querySelector(".btn-right2"),
      slider2 = document.querySelector("#slider2"),
      sliderSection2 = document.querySelectorAll(".slider-section2");


btnLeft2.addEventListener("click", e => moveToLeft2())
btnRight2.addEventListener("click", e => moveToRight2())

setInterval(() => {
    moveToRight2()
}, 3000);


let operacion2 = 0,
    counter2 = 0,
    widthImg2 = 100 / sliderSection2.length;

function moveToRight2() {
    if (counter2 >= sliderSection2.length-1) {
        counter2 = 0;
        operacion2 = 0;
        slider2.style.transform = `translate(-${operacion2}%)`;
        slider2.style.transition = "none";
        return;
    } 
    counter2++;
    operacion2 = operacion2 + widthImg2;
    slider2.style.transform = `translate(-${operacion2}%)`;
    slider2.style.transition = "all ease .6s"
    
}  

function moveToLeft2() {
    counter2--;
    if (counter2 < 0 ) {
        counter2 = sliderSection2.length-1;
        operacion2 = widthImg2 * (sliderSection2.length-1)
        slider2.style.transform = `translate(-${operacion2}%)`;
        slider2.style.transition = "none";
        return;
    } 
    operacion2 = operacion2 - widthImg2;
    slider2.style.transform = `translate(-${operacion2}%)`;
    slider2.style.transition = "all ease .6s"
    
    
}   


/* */

const btnLeft3 = document.querySelector(".btn-left3"),
      btnRight3 = document.querySelector(".btn-right3"),
      slider3 = document.querySelector("#slider3"),
      sliderSection3 = document.querySelectorAll(".slider-section3");


btnLeft3.addEventListener("click", e => moveToLeft3())
btnRight3.addEventListener("click", e => moveToRight3())

setInterval(() => {
    moveToRight3()
}, 3000);


let operacion3 = 0,
    counter3 = 0,
    widthImg3 = 100 / sliderSection3.length;

function moveToRight3() {
    if (counter3 >= sliderSection3.length-1) {
        counter3 = 0;
        operacion3 = 0;
        slider3.style.transform = `translate(-${operacion3}%)`;
        slider3.style.transition = "none";
        return;
    } 
    counter3++;
    operacion3 = operacion3 + widthImg3;
    slider3.style.transform = `translate(-${operacion3}%)`;
    slider3.style.transition = "all ease .6s"
    
}  

function moveToLeft3() {
    counter3--;
    if (counter3 < 0 ) {
        counter3 = sliderSection3.length-1;
        operacion3 = widthImg3 * (sliderSection3.length-1)
        slider3.style.transform = `translate(-${operacion3}%)`;
        slider3.style.transition = "none";
        return;
    } 
    operacion3 = operacion3 - widthImg3;
    slider3.style.transform = `translate(-${operacion3}%)`;
    slider3.style.transition = "all ease .6s"
    
    
}   




