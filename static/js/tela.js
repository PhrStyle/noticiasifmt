listagit = ""
display1len = 0

listainsta = ""
display2len = 0

fetch("/getlistagithub").then(response => {response.json().then(data => {
    listagit = data
    })
})

fetch("/getlistainstagram").then(response => {response.json().then(data => {
    listainsta = data
    })
})

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

function atualizardisplay1(){
    display1len = display1len + 1
    if (display1len >= listagit.imgvid.length) {
        display1len = 0
    }
    imgorvid = listagit.imgvid[display1len]
    document.getElementById("display1").innerHTML = ""
    if (imgorvid.tipo == "Imagem") {
        document.getElementById("display1").innerHTML = '<img src="/static/github/' + imgorvid["name"] + '">'
    }else {
        if (imgorvid["name"].includes("Reproduzir")) {

            document.getElementById("display1").innerHTML = '<video id="videodisplay1" controls autoplay><source src="/static/github/' + imgorvid["name"] +'"></video>'
            fetch("/pararradio")
        }else {
            document.getElementById("display1").innerHTML = '<video id="videodisplay1" controls autoplay muted><source src="/static/github/' + imgorvid["name"] +'"></video>'
        }
        clearInterval(timer1);
	
	var media1 = document.getElementById('videodisplay1');

        media1.addEventListener("pause", function() {
            fetch("/iniciarradio")
            timer1 = setInterval(atualizardisplay1, 10000);
	    atualizardisplay1()
	});

    }
}

function atualizardisplay2(){
    display2len = display2len + 1
    if (display2len >= listainsta.imgvid.length) {
        display2len = 0
    }
    imgorvid2 = listainsta.imgvid[display2len]
    document.getElementById("display2").innerHTML = ""
    if (imgorvid2.tipo == "Imagem") {
        document.getElementById("display2").innerHTML = '<img src="/static/ifmtcuiabaoficial/' + imgorvid2["name"] +'">'
    }else {
        document.getElementById("display2").innerHTML = '<video id="videodisplay2" controls autoplay muted><source src="/static/ifmtcuiabaoficial/' + imgorvid2["name"] +'"></video>'
        clearInterval(timer2);

        var media2 = document.getElementById('videodisplay2');

        media2.addEventListener("pause", function() {
            timer2 = setInterval(atualizardisplay2, 10000);
            atualizardisplay2()
        });

    }
}


var timer1 = setInterval(atualizardisplay1, 10000);

var timer2 = setInterval(atualizardisplay2, 10000);

