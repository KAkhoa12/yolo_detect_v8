let fileInput = document.getElementById("file");
let image = document.getElementById("image");
let downloadButton = document.getElementById("download");
const previewButton = document.getElementById("preview");
const previewImage = document.getElementById("preview-image");
const predict_image = document.getElementById("predict_image");
const previewContainer = document.getElementById("preview_image-container");
const arow_image = document.getElementById("arow_image");
const arow_image_predict = document.getElementById("arow_image_predict");
let cropper = "";
let fileName = "";
fileInput.onchange = () => {
  previewImage.src = "";
  let reader = new FileReader();
  reader.readAsDataURL(fileInput.files[0]);
  download.classList.add("hidden");
  arow_image.classList.add("hidden")
  arow_image_predict.classList.add("hidden")
  predict_image.classList.add("hidden")
  previewContainer.style.display="none";
  reader.onload = () => {
    image.setAttribute("src", reader.result);
    if (cropper) {
      cropper.destroy();
    }
    cropper = new Cropper(image,{viewMode:3});
    cropper.setAspectRatio(1);
    cropper.setDragMode("move");
    previewButton.classList.remove("hidden")
    previewContainer.classList.remove("hidden")

  };
  fileName = fileInput.files[0].name.split(".")[0];

};


previewButton.addEventListener("click", (e) => {
  let imgSrc = cropper.getCroppedCanvas({}).toDataURL("image/jpeg");
  e.preventDefault();
  previewImage.src = imgSrc;
  downloadButton.classList.remove("hidden");
  arow_image.classList.remove("hidden");
  previewContainer.style.display="flex";


  downloadButton.download = `cropped_${fileName}.jpg`;
  downloadButton.setAttribute("href", imgSrc);
});
window.onload = () => {
  download.classList.add("hidden");
  previewButton.classList.add("hidden")
  arow_image.classList.add("hidden")
  arow_image_predict.classList.add("hidden")
  previewContainer.classList.add("hidden")

};