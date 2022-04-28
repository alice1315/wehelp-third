var data;

async function init(){
    await getData({method: "GET"});
    render();
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

function render(){
    let content = document.getElementById("content");

    for(let i = 0; i < data.length; i++){
        let textDiv = document.createElement("div");
        let picDiv = document.createElement("img");
        let hr = document.createElement("hr");

        textDiv.textContent = data[i]["message"];
        picDiv.src = data[i]["image_url"];

        content.appendChild(textDiv);
        content.appendChild(picDiv);
        content.appendChild(hr);
    }
}

function upload(){
    let btn = document.getElementById("upload");
    btn.addEventListener("click", handle_upload)
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
        location.reload();

    } else{
        console.log("No data");
    }
}

