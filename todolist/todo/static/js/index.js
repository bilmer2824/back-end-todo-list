let nav = document.querySelector(".todo_nav-btn")
let title = document.querySelector('.todo_nav-btn-title')
let item = document.querySelectorAll('.todo-item')
let img = document.querySelector('.todo_nav-btn-img')
let elm = document.querySelector('.icon_add-todo')
let btn_close = document.querySelector('.windows-form-btn-close')
let win = document.querySelector('.windows')
let add_btn = document.querySelector('.windows-form-btn-add')
let lbl_input = document.querySelectorAll('.windows-form-label-input')
let logo_1 = document.getElementById('logo_1')
let logo_2 = document.getElementById('logo_2')
let search_icon = document.querySelector(".header-content-search-icon")
let form_label = document.querySelector('.header-content-form-label')


const edit_todo = document.querySelectorAll('.todo-item-btn-edit')

const created = document.getElementById('windows-forms-created')
const updated = document.getElementById('windows-forms-updated')

edit_todo.forEach(el => {
    el.addEventListener('click', () => {
        updated.classList.add('active')
    })
});

search_icon.addEventListener("click", () => {
    form_label.classList.toggle('active');
})
btn_close.addEventListener('click', () => {
    win.classList.remove("active")
    created.classList.remove('active')
    updated.classList.remove('active')
})
elm.addEventListener('click', () => {
    win.classList.add("active")
    created.classList.add("active")
})
add_btn.addEventListener('click', () => {
    setTimeout(() => {
        lbl_input.forEach(el => {
            el.value = ""
        });
    }, 200);
    win.classList.remove("active")
})
let t = true
nav.addEventListener("click", () => {
    if (t) {
        let svb = logo_1.getAttribute("src")
        img.setAttribute("src", svb)
        title.innerHTML = "Сетка"
        item.forEach(element => {
            element.style.width = "100%"
        });
        t = false;
    }
    else {
        t = true;
        let svb = logo_2.getAttribute("src")
        img.setAttribute("src", svb)
        title.innerHTML = "Список"
        item.forEach(element => {
            element.style.width = "360px"
        });
    }
})


