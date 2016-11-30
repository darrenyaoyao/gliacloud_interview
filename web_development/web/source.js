test = ["11111", "22222", "33333", "44444", "55555", "66666"]

document.getElementById("target").addEventListener("click", function( event ) {
    // display the current click count inside the clicked div
    event.target.innerHTML = test[Math.floor((Math.random()*test.length)+1)];
    }, false);
