document.addEventListener("DOMContentLoaded", (e) => {
    
    let imgShow = document.getElementById("form-image-show")
    imgShow.addEventListener("click", (e) => {
        console.log("=======button clicked=======\n\nselect image button clicked\n\n============================")
        document.getElementById("form-image").click()
    })

    let img = document.getElementById("form-image");
    img.addEventListener("change", (e) => {
        
        let msgs = document.getElementsByClassName("form__image__msg");
        for (var i = 0; i < msgs.length; i++){
            msgs[i].style = "display:none";
        }

        let imgPreivew = document.getElementsByClassName("form__preview__wrapper")[0];
        imgPreivew.style = "display:flex";

        const [file] = img.files;
        if (file) {
            document.getElementsByClassName("form__preview")[0].src = URL.createObjectURL(file);
        }

    })
})