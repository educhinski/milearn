const colors = ["green", "red", "rgba(133,122,200)", "#f15025"];

const btn = document.getElementById('btn');
const color = document.querySelector('.color');
color.textContent = '#f1f5f8';

btn.addEventListener('click', function () {
    // get random number between 0 and length of array
    const randomNumber = getRandomNumber();

    document.body.style.backgroundColor = colors[randomNumber];
    color.textContent = colors[randomNumber];
    console.log(color.textContent);
    if (color.textContent[0] !== '#') {
        color.style.textTransform = 'lowercase';
    }
    else {
        color.style.textTransform = 'uppercase';
    }
});

function getRandomNumber() {
    return Math.floor(Math.random() * colors.length);
}
