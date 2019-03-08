
//
// Today's tea: https://developers.google.com/web/updates/2017/09/autoplay-policy-changes
//

var song = document.querySelector("#song");
var playbutton = document.querySelector("#playbutton");
var cursedimage = document.querySelector("#cursedimage");

playbutton.addEventListener("click", function() {
    playbutton.classList.add("hidden");
    cursedimage.classList.remove("hidden");
    song.play();
});

var promise = song.play();

if (promise !== undefined) {
    promise.then(_ => {
        // Autoplay started!
        cursedimage.classList.remove("hidden");
    }).catch(error => {
        // Autoplay was prevented.
        // Show a "Play" button so that user can start playback.
        playbutton.classList.remove("hidden");
    });
}

