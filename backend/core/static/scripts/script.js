function showSection(section) {   
    fetch(`/sections/${section}`)
    .then(response => response.text())
    .then(text => {
        console.log(text);
        document.querySelector('#content').textContent = text;
    });

}

document.addEventListener("DOMContentLoaded", function() {
    document.querySelectorAll('a').forEach(a => {
        a.onclick = function() {
            showSection(this.dataset.section)
        }
    })
});
