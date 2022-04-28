var data;
var content = document.getElementById("content");

async function init(){
    await getData({method: "GET"});
    renderAll();
    upload();
}

async function getData(fetchOptions){
    await fetch("/api/messages", fetchOptions)
    .then((resp) => {
        return resp.json();
    }).then((result) => {
        data = result["data"];
    })
}

function render(message, image_url){
    let container = document.createElement("div");
    let textDiv = document.createElement("div");
    let picDiv = document.createElement("img");
    let hr = document.createElement("hr");

    textDiv.textContent = message;
    picDiv.src = image_url;

    content.insertBefore(container, content.firstChild);
    container.appendChild(textDiv);
    container.appendChild(picDiv);
    container.appendChild(hr);
}

function renderAll(){
    for(let i = 0; i < data.length; i++){
        render(data[i]["message"], data[i]["image_url"]);
    }
}

function upload(){
    let btn = document.getElementById("upload");
    btn.addEventListener("click", handle_upload);
}

async function handle_upload(event){
    event.preventDefault()
    let message = document.querySelector("input[type=text]").value;
    let file = document.querySelector("input[type=file]").files[0];

    if(message && file){
        let formData = new FormData()
        formData.append("message", message)
        formData.append("file", file)

        let fetchOptions = {
            method: "POST",
            body: formData,
        }

        await getData(fetchOptions);

        render(data["message"], data["image_url"]);

    } else{
        console.log("No data");
    }
}
