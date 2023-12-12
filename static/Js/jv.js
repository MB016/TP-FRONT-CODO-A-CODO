const API_URL = "https://sheetdb.io/api/v1/cdnzb7hmxs0ug"

document.querySelector("form").addEventListener("submit", async (e) => {
    e.preventDefault();

    const form = document.querySelector("form");

    let dataForm = new FormData(form);

    dataForm.append("ticket_time", new Date().toString());

    await fetch(API_URL, {
        method: "POST",
        body: dataForm,
    });

    form.classList.add("animation");

    alert("Ya estas registrado");
    window.location.href = "/"; 
   
});