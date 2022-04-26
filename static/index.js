var data;

var text;
var file;

async function init(){
    // getData();
    // upload();
    await testGetData();
    testRender();
}

async function testGetData(){
    await fetch("/api/messages", {method: "GET"})
    .then((resp) => {
        return resp.json();
    }).then((result) => {
        data = result["data"];
    })
}

function testRender(){
    let content = document.getElementById("content");

    for(let i = 0; i < data.length; i++){
        let textDiv = document.createElement("div");
        let picDiv = document.createElement("div");
        let hr = document.createElement("hr");

        textDiv.textContent = data[i]["message"];
        picDiv.textContent = data[i]["image_url"];

        content.appendChild(textDiv);
        content.appendChild(picDiv);
        content.appendChild(hr);
    }
}

function getData(){
    let text = document.querySelector("input[type=text]").value;
    let file = document.querySelector("input[type=file]")
}

function render(){
    let content = document.getElementById("content");
    let textDiv = document.createElement("div");
    let picDiv = document.createElement("img");
    let hr = document.createElement("hr");

    textDiv.textContent = text;
    picDiv.textContent = file;

    content.appendChild(textDiv);
    content.appendChild(picDiv);
    content.appendChild(hr);
    
}

function upload(){
    let btn = document.getElementById("upload");
    btn.addEventListener("click", function(){
        text = document.querySelector("input[type=text]").value;
        file = document.querySelector("input[type=file]").files.name;
        render();
    })
}

