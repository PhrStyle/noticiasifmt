var media = document.getElementById('teste');
listadevi = ""
fetch("/getlista").then(response => {response.json().then(data => {
    listadevi = data
    })
})
// Playing event
media.addEventListener("playing", function() {
    console.log("Playing event triggered");
});

// Pause event
media.addEventListener("pause", function() {
    console.log(listadevi);
});