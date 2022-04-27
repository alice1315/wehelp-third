var data;

var message;
var file;

function init(){
    upload();
    // await getData();
    // testRender();
}

async function getData(fetchOptions){
    await fetch("/api/messages", fetchOptions)
    .then((resp) => {
        return resp.json();
    }).then((result) => {
        // data = result["data"];
        console.log(result);
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

function render(){
    let content = document.getElementById("content");
    let textDiv = document.createElement("div");
    let picDiv = document.createElement("img");
    let hr = document.createElement("hr");

    textDiv.textContent = message;
    picDiv.textContent = file;

    content.appendChild(textDiv);
    content.appendChild(picDiv);
    content.appendChild(hr);
    
}

function upload(){
    let btn = document.getElementById("upload");
    btn.addEventListener("click", handle_upload)
}

async function handle_upload(event){
    event.preventDefault()
    message = document.querySelector("input[type=text]").value;
    file = document.querySelector("input[type=file]").files[0];

    let formData = new FormData()
    formData.append("message", message)
    formData.append("file", file)

    let fetchOptions = {
        method: "POST",
        body: formData,
    }

    await getData(fetchOptions);
}

