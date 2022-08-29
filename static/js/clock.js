const strips = [...document.querySelectorAll(".strip")];
const numberSize = "4"; // in rem
const start_day = new Date("04/26/2022 0:0:0");
// highlight number i on strip s for 1 second
function highlight(strip, d) {
    strips[strip]
        .querySelector(`.number:nth-of-type(${d + 1})`)
        .classList.add("pop");

    setTimeout(() => {
        strips[strip]
            .querySelector(`.number:nth-of-type(${d + 1})`)
            .classList.remove("pop");
    }, 950); // causes ticking
}

function stripSlider_date(strip, number) {
    let d1 = Math.floor(number / 100);
    let d2 = Math.floor((number - d1*100) / 10);
    let d3 =  Math.floor(number % 10);
    
    strips[strip].style.transform = `translateY(${d1 * -numberSize}vmin)`;
    highlight(strip, d1);
    strips[strip + 1].style.transform = `translateY(${d2 * -numberSize}vmin)`;
    highlight(strip + 1, d2);
    strips[strip + 2].style.transform = `translateY(${d3 * -numberSize}vmin)`;
    highlight(strip + 2, d3);
}

function stripSlider(strip, number) {
    let d1 = Math.floor(number / 10);
    let d2 = number % 10;

    strips[strip].style.transform = `translateY(${d1 * -numberSize}vmin)`;
    highlight(strip, d1);
    strips[strip + 1].style.transform = `translateY(${d2 * -numberSize}vmin)`;
    highlight(strip + 1, d2);
}

setInterval(() => {
    // get new time
    const time = new Date();

    // get h,m,s
    const diff= time.getTime() - start_day.getTime()
    const day = Math.floor(diff / 1000 / 60 / 60/24);
    const hours = time.getHours();
    const mins = time.getMinutes();
    const secs = time.getSeconds();

    // slide strips
    stripSlider_date(0, day);
    stripSlider(3, hours);
    stripSlider(5, mins);
    stripSlider(7, secs);

    // highlight numbers
}, 1000);