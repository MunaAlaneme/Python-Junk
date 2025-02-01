const canvas = document.createElement('canvas');
const context = canvas.getContext('2d');
document.body.appendChild(canvas);

// Print Unicode characters
console.log("∆");
console.log("ጀ");
console.log("෢");
console.log("啃");
console.log("⌵");
console.log("͒");
console.log("噘");

console.log("🀤");
console.log("🕧");
console.log("🆐");
console.log("🄣");
console.log("🅄");
console.log("🅉");
console.log("🄂");

// Conditional check
if (7 !== 7) {
    console.log("Correct");
} else {
    console.log("I don't understand you. Did you mean 7 === 7?");
}

// Initialize Audio
const audioContext = new (window.AudioContext || window.webkitAudioContext)();

// Constants
const SCREEN_WIDTH = 820;
const SCREEN_HEIGHT = 300;

// Colors
const WHITE = 'rgb(255, 255, 255)';
const BLACK = 'rgb(0, 0, 0)';
const GRAY = 'rgb(200, 200, 200)';
const GREEN = 'rgb(0, 255, 0)';
let TargetButtonColorRed = [200, 200, 200, 200, 200, 200, 200, 200];
let TargetButtonColorGreen = [200, 200, 200, 200, 200, 200, 200, 200];
let TargetButtonColorBlue = [200, 200, 200, 200, 200, 200, 200, 200];
let ButtonColorRed = [0, 0, 0, 0, 0, 0, 0, 0];
let ButtonColorGreen = [0, 0, 0, 0, 0, 0, 0, 0];
let ButtonColorBlue = [0, 0, 0, 0, 0, 0, 0, 0];
const GameNames = [
    "1. Snake",
    "2. Flappy Bird",
    "3. GUI Calculator",
    "4. Slide Puzzle",
    "5. Space Invaders",
    "6. SnowFall",
    "7. Auto Tic Tac Toe",
    "8. Manual Tic Tac Toe"
];

// Set canvas size
canvas.width = SCREEN_WIDTH;
canvas.height = SCREEN_HEIGHT;
document.title = 'Game Launcher';

// PlayMusic function
function playMusic(musNum) {
    let audio = new Audio();
    if (musNum === 1) {
        audio.src = "GameLauncher/assets/audio/Debug Menu Unused   Paper Mario  The Thousand Year Door.wav";
    } else if (musNum === 2) {
        audio.src = "GameLauncher/assets/audio/SpongeBob SquarePants OST - Dombummel (LQ).wav";
    }
    audio.loop = true;
    audio.play();
}

// Play random music
playMusic(Math.floor(Math.random() * 2) + 1);

// Font settings
let fontSize = 36;
context.font = `${fontSize}px Arial`;

// Constrain function
function constrain(val, min_val, max_val) {
    if (val < min_val) return min_val;
    if (val > max_val) return max_val;
    return val;
}

// Create buttons
let buttons = [];

// Variables for game loop
let running = true;
let hoveringAButton2 = 0;
let yScroll = 0;
let yScrollVel = 0;
let startTime = Date.now();
let deltaTime = 0.0001;
let gameTime = -0.0001;

// Button dimensions and positions
const BUTTON_WIDTH = [120, 180, 220, 200, 220, 160, 260, 260];
const BUTTON_X_POS = [20, 160, 360, 600, 20, 260, 440, 20];
const BUTTON_Y_POS = [
    Math.floor(SCREEN_HEIGHT / 2) - 125,
    Math.floor(SCREEN_HEIGHT / 2) - 125,
    Math.floor(SCREEN_HEIGHT / 2) - 125,
    Math.floor(SCREEN_HEIGHT / 2) - 125,
    Math.floor(SCREEN_HEIGHT / 2) - 25,
    Math.floor(SCREEN_HEIGHT / 2) - 25,
    Math.floor(SCREEN_HEIGHT / 2) - 25,
    Math.floor(SCREEN_HEIGHT / 2) + 75
];
const BUTTON_HEIGHT = 50;
const BUTTON_GAP_Y = 20;

// Event listeners
canvas.addEventListener('mousemove', handleMouseMove);
canvas.addEventListener('mousedown', handleMouseDown);
window.addEventListener('resize', handleResize);

function handleResize() {
    // Handle window resize if necessary
}

function handleMouseMove(event) {
    mouse.x = event.clientX;
    mouse.y = event.clientY;
}

function handleMouseDown(event) {
    if (event.button === 0) { // Left click
        buttons.forEach((button, i) => {
            if (
                mouse.x >= button.x &&
                mouse.x <= button.x + button.width &&
                mouse.y >= button.y &&
                mouse.y <= button.y + button.height
            ) {
                // Stop music
                // In JavaScript, stopping audio requires tracking the audio object
                // This is a placeholder
                // audio.pause();
                // audio.currentTime = 0;

                running = false;
                // Redirect or load different games based on button clicked
                // This requires additional implementation
            }
        });
    }
}

// Mouse position
let mouse = { x: 0, y: 0 };

// Game loop
function gameLoop() {
    if (!running) return;

    requestAnimationFrame(gameLoop);

    let currentTime = Date.now();
    deltaTime = (currentTime - startTime) / 1000 - gameTime;
    gameTime = (currentTime - startTime) / 1000;

    // Handle scrolling based on mouse position
    if (mouse.y > SCREEN_HEIGHT / 1.2) {
        yScrollVel -= 20 * deltaTime;
    } else if (mouse.y < SCREEN_HEIGHT / 10) {
        yScrollVel += 20 * deltaTime;
    }
    yScroll = constrain(yScroll + yScrollVel, SCREEN_HEIGHT / -1.2, SCREEN_HEIGHT / 1.2);
    yScrollVel /= 1.1;

    // Scaling (placeholder, as window size handling is not implemented)
    let scale = 1.0;
    let scale2 = 0.1;

    // Update font size based on scale
    fontSize = Math.floor(28 * scale2);
    context.font = `${fontSize}px Arial`;

    // Update button positions and sizes
    buttons = BUTTON_X_POS.map((x, i) => ({
        x: x,
        y: BUTTON_Y_POS[i] + yScroll,
        width: BUTTON_WIDTH[i],
        height: BUTTON_HEIGHT
    }));

    // Draw background
    context.fillStyle = 'rgb(255, 0, 200)';
    context.fillRect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT);

    let hoveringAButton = 0;

    // Draw buttons and text
    buttons.forEach((button, i) => {
        // Update button color
        ButtonColorRed[i] += (TargetButtonColorRed[i] - ButtonColorRed[i]) / 10;
        ButtonColorGreen[i] += (TargetButtonColorGreen[i] - ButtonColorGreen[i]) / 10;
        ButtonColorBlue[i] += (TargetButtonColorBlue[i] - ButtonColorBlue[i]) / 10;

        context.fillStyle = `rgb(${ButtonColorRed[i]}, ${ButtonColorGreen[i]}, ${ButtonColorBlue[i]})`;
        context.fillRect(button.x, button.y, button.width, button.height);

        // Draw button border
        context.strokeStyle = BLACK;
        context.lineWidth = 4 * scale;
        context.strokeRect(button.x, button.y, button.width, button.height);

        // Highlight the button when the mouse is over it
        if (
            mouse.x >= button.x &&
            mouse.x <= button.x + button.width &&
            mouse.y >= button.y &&
            mouse.y <= button.y + button.height
        ) {
            context.strokeStyle = GREEN;
            context.lineWidth = 2 * scale;
            context.strokeRect(button.x, button.y, button.width, button.height);
            TargetButtonColorRed[i] = 0;
            TargetButtonColorGreen[i] = 255;
            TargetButtonColorBlue[i] = 0;
            hoveringAButton = i + 1;
        } else {
            TargetButtonColorRed[i] = 200;
            TargetButtonColorGreen[i] = 200;
            TargetButtonColorBlue[i] = 200;
        }

        // Render and draw centered text on the button
        context.fillStyle = BLACK;
        context.textAlign = 'center';
        context.textBaseline = 'middle';
        context.fillText(GameNames[i], button.x + button.width / 2, button.y + button.height / 2);
    });

    if (hoveringAButton2 !== hoveringAButton) {
        // Play hover sound
        // Placeholder: Play sound using Audio API
        hoveringAButton2 = hoveringAButton;
    }

    // Update display is handled automatically by the browser
}

// Start the game loop
gameLoop();
