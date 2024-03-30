const  listNavbar = [
    {
        "path":"/",
        "name":"Home"
    },
    {
        "path":"/models/",
        "name":"Model Machine learning"
    },
    {
        "path":"#",
        "name":"Blog"
    },
    {
        "path":"#",
        "name":"About me"
    }
]

const navbar = document.querySelector("#navbar .navbar-items");
const navbarleft = document.querySelector(".sidebar-items-left")

listNavbar.forEach(item => {
    const link = `<a href="${item.path}" class="mr-5 font-medium hover:text-gray-900">${item.name}</a>`;
    navbar.insertAdjacentHTML('beforeend', link);
});

listNavbar.forEach(item => {
    const link = `<a href="${item.path}" class="mr-5 text-4xl font-thin">${item.name}</a>`;
    navbarleft.insertAdjacentHTML('beforeend', link);
});
