document.addEventListener("DOMContentLoaded", function () {
    const content = document.querySelector(".md-content");

    if (content) {
        const path = window.location.pathname
                .replace(/^\/notes\//, '')        // remove base path
                .replace(/\/$/, '')               // remove trailing slash
            || 'index';

        const mdFile = path + ".md";

        const editLink = document.createElement("a");
        editLink.href = `/notes/${mdFile}/edit`;
        editLink.textContent = "✏️ Edit this page";
        editLink.style.display = "inline-block";
        editLink.style.marginBottom = "1rem";
        editLink.style.float = "right";

        content.prepend(editLink);
    }
});
