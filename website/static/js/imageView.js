// Image preview functionality
// References to HTML elements
const Upload = document.getElementById("Upload");
const previewContainer = document.getElementById("imageView");
const previewImage = previewContainer.querySelector(".image-preview__image")
const previewDefaultText = previewContainer.querySelector(".image-preview__default-text")

// Get correspondent object for selected file
Upload.addEventListener("change", function() {
    const file = this.files[0]; // This refers to file input

    if (file) {
        const reader = new FileReader(); // Read chosen file as data url

        previewDefaultText.style.display = "none";
        previewImage.style.display = "block";

        // Tell reader to load the file
        reader.addEventListener("load", function() {
            //console.log(this);
            previewImage.setAttribute("src", this.result)
        });

        // When file is loaded, insert read data url as source
        reader.readAsDataURL(file);

        const dict_values = { "image": file };  // Proper object format
        console.log("Sending JSON:", JSON.stringify(dict_values));  // Debugging log

        $.ajax({
            url: "/test",
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify(dict_values),
            dataType: "json",
            success: function(response) {
                console.log("Image sent successfully:", response);
            },
            error: function(xhr, status, error) {
                console.error("Error:", xhr.responseText);
            }
        });

    }
    // if no file is selected, go back to css default
    else {
        previewDefaultText.style.display = "null";
        previewImage.style.display = "null";
        previewImage.setAttribute("src","");
    }
});