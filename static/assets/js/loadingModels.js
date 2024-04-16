const listModels = [
    {
        "name": "Algorithm YOLO version 8 ",
        "path": "/model/yolo/",
        "type":"AI / MACHINE LEARNING",
        "description":"Using the yolo v8 model to detect the first media in Ho Chi Minh City",
        "image":"icons8-artificial-intelligence-100.png"
    },
    {
        "name": "GAN adversarial generative network of Face2comics dataset",
        "path": "/model/gan/",
        "type":"AI / COMPUTER VISION",
        "description":"Use an adversarial network to generate images from the face2comics dataset",
        "image":"icons8-artificial-intelligence-100.png"
    },
    {
        "name": "GAN adversarial generative network of Celeb-A-Mask HQ dataset",
        "path": "#",
        "type":"AI / COMPUTER VISION",
        "description":"Use an adversarial network to generate images from the Celeb-A-Mask HQ dataset",
        "image":"icons8-artificial-intelligence-100.png"
    },
]
const listLogo = [
    "pytorch-logo.png",
    "tensorflow-logo.png",
    "keras-logo.png",
    "react-logo.png",
    "html-logo.png",
    "css-logo.png",
    "js-logo.png",
    "mongo-logo.png",
    "django-logo.png",
]
const modelsContainer = document.querySelector("#models");
const logoContainer = document.querySelector("#logo-container");
listModels.map((item, index) => {
    let template;
    if (index % 2 === 0) {
        template = `
            <a href="${item.path}" class="bg-gray-100 group lg:h-64 md:h-auto  relative cursor-pointer rounded-br-none rounded-3xl p-6">
                <div class="w-3/4">
                    <h1 class="font-semibold group-hover:underline text-2xl">${item.name}</h1>
                    <span class="inline-block bg-black rounded-full bg-black w-8 h-8 mt-4 text-lime-400 flex items-center justify-center">
                        <i class="ri-arrow-right-up-line text-2xl"></i>
                    </span>
                </div>
                <span class="absolute bg-lime-400 h-24 w-24 rounded-tl-3xl bottom-0 right-0 p-3">
                    <img src="/static/assets/images/${item.image}" alt="image for models ${item.name}">
                </span>
            </a>
        `
    } else {
        template = `
        <a href="${item.path}" class="bg-black lg:h-64 md:h-auto group  relative cursor-pointer rounded-br-none rounded-3xl p-6">
            <div class="w-3/4">
                <h1 class="font-semibold group-hover:underline text-white text-3xl">${item.name}</h1>
                <span class="inline-block rounded-full bg-white w-8 h-8 mt-4 text-black flex items-center justify-center">
                    <i class="ri-arrow-right-up-line text-2xl"></i>
                </span>
            </div>
            <span class="absolute bg-lime-400 h-24 w-24 rounded-tl-3xl bottom-0 right-0 p-3">
                <img src="/static/assets/images/${item.image}" alt="image for models ${item.name}">
            </span>
        </a>
        `
    }

    modelsContainer.insertAdjacentHTML('beforeend', template);
})

listLogo.map((item) => {
    const template = `
            <li class="card h-full">
                <img class="h-32 max-sm:w-full grayscale hover:grayscale-0 transition-all duration-500 object-cover" src="/static/assets/images/${item}" />  
            </li>
        `
    logoContainer.insertAdjacentHTML('beforeend', template);
})