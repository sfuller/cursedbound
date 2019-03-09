
//
// Today's tea: https://developers.google.com/web/updates/2017/09/autoplay-policy-changes
//

let song = document.querySelector("#song");
let playbutton = document.querySelector("#playbutton");
let cursedimage = document.querySelector("#cursedimage");
let cursedlink = document.querySelector("#cursedimage a");

let play = function() {
    playbutton.classList.add("hidden");
    cursedimage.classList.remove("hidden");
    if (song.paused || song.ended) {
        song.play();
    }
};

let pause = function() {
    playbutton.classList.remove("hidden");
    cursedimage.classList.add("hidden");
    song.pause();
};

playbutton.addEventListener("click", function() {
    play();
});

if (cursedlink !== null) {
    cursedlink.addEventListener("click", function() {
        pause();
    })
}


let promise = song.play();

if (promise !== undefined) {
    promise.then(_ => {
        // Autoplay started!
        play();
    }).catch(error => {
        // Autoplay was prevented.
        pause();
    });
}







