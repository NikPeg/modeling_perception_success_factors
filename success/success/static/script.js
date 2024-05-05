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
    const sandwichContainer = document.querySelector('.sandwich-container');
    const nameLength = nameElement.textContent.length;
    console.log(nameLength);
    upperContainer.style.setProperty('--name-length', nameLength);
    sandwichContainer.style.setProperty('--name-length', nameLength);
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

    const sandwichElement = document.getElementById("sandwich");
    console.log(sandwichElement.style.display);
    if (!sandwichElement.style.display) {
        sandwichElement.style.display = "flex";
    }
    else {
        sandwichElement.style.display = null;
    }
}

function showFactorPopup() {
    console.log('add factor!');
    document.getElementById("projectBackgroundOverlay").style.display = "block";
    document.getElementById("factorPopup").style.display = "block";
}

function hideFactorPopup() {
    document.getElementById("projectBackgroundOverlay").style.display = "none";
    document.getElementById("factorPopup").style.display = "none";
}

function showEdgePopup() {
    console.log('add edge!');
    document.getElementById("projectBackgroundOverlay").style.display = "block";
    document.getElementById("edgePopup").style.display = "block";
}

function hideEdgePopup() {
    document.getElementById("projectBackgroundOverlay").style.display = "none";
    document.getElementById("edgePopup").style.display = "none";
}

function delete_entity() {
    window.alert("Press any entity to delete it.");
    console.log('delete!');
}

function export_project() {
    console.log('export!');
}

function save_project() {
    console.log('save!');
}