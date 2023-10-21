document.getElementById("id_image").addEventListener("change", function () {
        var input = this;
        var img = document.getElementById("preview-image");
        if (input.files && input.files[0]) {
            var reader = new FileReader();
            reader.onload = function (e) {
                img.src = e.target.result;
            };
            reader.readAsDataURL(input.files[0]);
        } else {
            img.src = "";
        }
    });