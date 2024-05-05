function showLoginPopup() {
    document.getElementById("backgroundOverlay").style.display = "block";
    document.getElementById("loginPopup").style.display = "block";
}
function hideLoginPopup() {
    document.getElementById("backgroundOverlay").style.display = "none";
    document.getElementById("loginPopup").style.display = "none";
}
function showRegisterPopup() {
    document.getElementById("backgroundOverlay").style.display = "block";
    document.getElementById("registerPopup").style.display = "block";
}
function hideRegisterPopup() {
    document.getElementById("backgroundOverlay").style.display = "none";
    document.getElementById("registerPopup").style.display = "none";
}
function showCreatePopup() {
    document.getElementById("backgroundOverlay").style.display = "block";
    document.getElementById("createPopup").style.display = "block";
}
function hideCreatePopup() {
    document.getElementById("backgroundOverlay").style.display = "none";
    document.getElementById("createPopup").style.display = "none";
}

function updateContainerWidth() {
    const nameElement = document.querySelector('.top-left-label');
    const upperContainer = document.querySelector('.upper-container');
    const nameLength = nameElement.textContent.length;
    console.log(nameLength);
    upperContainer.style.setProperty('--name-length', nameLength);
}

// Call the function initially
updateContainerWidth();

function play() {
    console.log('playing!');
}

function pause() {
    console.log('pause!');
}

function sandwich() {
    console.log('sandwich!');
}

function add_factor() {
    console.log('add factor!');
}

function add_edge() {
    console.log('add edge!');
}

function delete_entity() {
    console.log('delete!');
}