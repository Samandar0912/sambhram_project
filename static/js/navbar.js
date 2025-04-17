document.addEventListener("DOMContentLoaded", (event) => {

    let ul_btn = document.querySelector(".ul_1 button");
    let ul_1 = document.querySelector(".ul_1");
    let gamburger = document.querySelector(".gamburger");

    if (gamburger && ul_1) {
        gamburger.addEventListener("click", () => {
            ul_1.style.display = "block";
            console.log("yoo");
        });
    }

    if (ul_btn) {
        ul_btn.addEventListener("click", () => {
            ul_1.style.display = "none";
        });
    }
});