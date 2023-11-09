//const socket = new WebSocket('ws://10.100.12.221:8000/ws/some_path/');
const socket = new WebSocket('ws://192.168.1.179:8000/ws/some_path/');
//10.100.12.221 Université
//192.168.1.179 Maison 


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




// Initialiser la variable pour stocker la couleur actuelle
let currentColor = '#000000';  // Noir par défaut
let pixelCounter = 0;

// ...

function showColorPicker(event, pixelId) {
    // Mettre la couleur actuelle dans l'élément input de type couleur
    const colorPicker = document.getElementById(`color-${pixelId}`);
    colorPicker.value = currentColor;

    const colorPickerForm = document.getElementById(`color-picker-${pixelId}`);
    const overlay = document.getElementById('overlay-modal');
    overlay.style.display = 'block';
    const clickX = event.clientX + window.pageXOffset ;
    const clickY = event.clientY + window.pageYOffset - 50;

    colorPickerForm.style.top = `${clickY}px`;
    colorPickerForm.style.left = `${clickX}px`;


    colorPickerForm.style.display = 'block';
}


function cancelColorPicker(pixelId) {
    document.getElementById(`color-picker-${pixelId}`).style.display = 'none';
    document.getElementById('overlay-modal').style.display = 'none';
}



function changePixelColor(pixelId) {
    const colorPicker = document.getElementById(`color-${pixelId}`);
    const newColor = colorPicker.value;

    // Mettre à jour la couleur actuelle avec la nouvelle couleur choisie
    currentColor = newColor;

    socket.send(JSON.stringify({
        'pixel_id': pixelId,
        'color': newColor,
    }));
    
    // Incrémenter le compteur de pixels
    pixelCounter++;
    
    localStorage.setItem('pixelCounter', pixelCounter);

    // Mettre à jour l'élément HTML avec la nouvelle valeur du compteur
    document.getElementById('pixel-counter').textContent = pixelCounter;

    document.getElementById(`color-picker-${pixelId}`).style.display = 'none';
    document.getElementById('overlay-modal').style.display = 'none';

}

document.addEventListener("DOMContentLoaded", function() {
    document.body.classList.add("loaded");
    
    const savedCounter = localStorage.getItem('pixelCounter');

    // Vérifier si la valeur du compteur existe dans le localStorage
    if (savedCounter !== null) {
        // Si elle existe, mettre à jour le compteur avec la valeur du localStorage
        pixelCounter = parseInt(savedCounter);
    }

    // Mettre à jour l'élément HTML avec la valeur actuelle du compteur
    document.getElementById('pixel-counter').textContent = pixelCounter;
    
    // Vérifier si la date de première visite est stockée dans localStorage
if (!localStorage.getItem('firstVisit')) {
    // Si ce n'est pas le cas, stocker la date et l'heure actuelles
    const firstVisitTime = new Date().getTime();
    localStorage.setItem('firstVisit', firstVisitTime);
}




    // ... (votre code existant)
});



// Récupérer la date et l'heure de la première visite depuis localStorage
const firstVisitTime = parseInt(localStorage.getItem('firstVisit'));
const firstVisitDate = new Date(firstVisitTime);




const imagePreview = document.getElementById('previewImage');
const deleteButton = document.getElementById('deleteButton');

imagePreview.addEventListener('dragstart', function(event) {
    // Définir les données de l'élément en cours de déplacement
    event.dataTransfer.setData('text/plain', 'Cet élément peut être glissé');
});

imagePreview.addEventListener('drag', function(event) {
    // Récupérer la position de la souris
    const mouseX = event.clientX;
    const mouseY = event.clientY;

    // Définir la position de l'image en fonction de la position de la souris
    imagePreview.style.left = mouseX + 'px';
    imagePreview.style.top = mouseY + 'px';
});






















