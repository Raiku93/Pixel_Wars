const socket = new WebSocket('ws://192.168.1.158:8000/ws/some_path/');

socket.onmessage = (event) => {
    const data = JSON.parse(event.data);
    const pixelId = data.pixel_id;
    const newColor = data.color;
    const pixelElement = document.getElementById(`pixel-${pixelId}`);
    pixelElement.style.backgroundColor = newColor;

    document.querySelector('.battle-title').classList.add('updated');

    setTimeout(() => {
        document.querySelector('.battle-title').classList.remove('updated');
    }, 500);
};

function showColorPicker(event, pixelId) {
    const colorPickerForm = document.getElementById(`color-picker-${pixelId}`);
    const overlay = document.getElementById('overlay');

    const clickX = event.clientX + window.pageXOffset + 10;
    const clickY = event.clientY + window.pageYOffset - 50;

    colorPickerForm.style.top = `${clickY}px`;
    colorPickerForm.style.left = `${clickX}px`;

    overlay.style.display = 'block';
    colorPickerForm.style.display = 'block';
}

function cancelColorPicker(pixelId) {
    document.getElementById(`color-picker-${pixelId}`).style.display = 'none';
    document.getElementById('overlay').style.display = 'none';
}

function changePixelColor(pixelId) {
    const colorPicker = document.getElementById(`color-${pixelId}`);
    const newColor = colorPicker.value;

    socket.send(JSON.stringify({
        'pixel_id': pixelId,
        'color': newColor,
    }));

    document.getElementById(`color-picker-${pixelId}`).style.display = 'none';
    document.getElementById('overlay').style.display = 'none';
}

document.addEventListener("DOMContentLoaded", function() {
    document.body.classList.add("loaded");
});

