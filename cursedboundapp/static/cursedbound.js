
//
// Today's tea: https://developers.google.com/web/updates/2017/09/autoplay-policy-changes
//

const song = document.querySelector("#song");
const playbutton = document.querySelector("#playbutton");
const cursedimage = document.querySelector("#cursedimage");
const cursedlink = document.querySelector("#cursedimage a");

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

// Not using react... yet

// const e = React.createElement;
//
// const Button = function({text}) {
//     return e('a', {className: 'link'}, text);
// };
//
// const Menu = function({}) {
//     return e('div', {className: 'links'},
//         e(Button, {text: 'About'}),
//         e(Button, {text: 'Suggestions'}),
//         e(Button, {text: 'Link'}),
//         e(Button, {text: 'Context'}),
//     );
// };

//ReactDOM.render(e(Menu, {}), document.getElementById('react_root'));

function copy_permalink_to_clipboard() {
    // Some of the worst javascript I have ever written.
    const image_id_input = document.getElementById('image_id_input');
    image_id_input.style.display = "block";
    if (!image_id_input.value.startsWith(location.protocol)) {
        image_id_input.value = location.protocol + '//' + location.host + '/' + image_id_input.value;
    }
    image_id_input.select();
    document.execCommand('copy')
    image_id_input.style.display = "none";
    alert('A link to this specific "Encounter" has (hopefully) been copied to your clipboard.');
}