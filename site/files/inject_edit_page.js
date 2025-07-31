document.addEventListener("DOMContentLoaded", function () {
    const content = document.querySelector(".md-content");

    if (content) {
        const path = window.location.pathname
                .replace(/^\/notes\//, '')        // remove base path
                .replace(/\/$/, '')               // remove trailing slash
            || 'index';

        const mdFile = path + ".md";

        // ✏️ Edit link
        const editLink = document.createElement("a");
        editLink.href = `/notes/${mdFile}/edit`;
        editLink.textContent = "✏️ Edit this page";
        editLink.style.display = "inline-block";
        editLink.style.marginRight = "1rem";

        // ➕ Add Page link
        const addLink = document.createElement("a");
        addLink.href = `/notes/new_page`;
        addLink.textContent = "➕ Add New Page";
        addLink.style.display = "inline-block";

        // Wrap in a container
        const toolbar = document.createElement("div");
        toolbar.style.marginBottom = "1rem";
        toolbar.style.textAlign = "right";
        toolbar.appendChild(editLink);
        toolbar.appendChild(addLink);

        content.prepend(toolbar);
    }
});
