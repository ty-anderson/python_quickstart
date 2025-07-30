import os
from flask import Flask, render_template, request, jsonify, redirect, send_from_directory, abort
import subprocess

app = Flask(__name__)

# Set base paths relative to this file
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
MARKDOWN_DIR = os.path.join(BASE_DIR, "docs")
SITE_DIR = os.path.join(BASE_DIR, "site")

@app.route("/")
def home():
    return redirect("/notes/")


@app.route("/notes/")
def serve_index():
    return send_from_directory(SITE_DIR, "index.html")


@app.route("/notes/<path:filename>")
def serve_notes_static(filename):
    # If it's a directory, append "index.html"
    full_path = os.path.join(SITE_DIR, filename)

    if os.path.isdir(full_path):
        full_path = os.path.join(full_path, "index.html")
        filename = os.path.relpath(full_path, SITE_DIR)

    if not os.path.exists(os.path.join(SITE_DIR, filename)):
        # print("❌ Not found:", os.path.join(SITE_DIR, filename))
        return "Not Found", 404

    # print("✅ Serving:", os.path.join(SITE_DIR, filename))
    return send_from_directory(SITE_DIR, filename)


@app.route("/notes/<path:filename>/edit", methods=["GET", "POST"])
def edit(filename):
    # Ensure .md extension
    if not filename.endswith(".md"):
        filename += ".md"

    # Secure and resolve file path
    source_file = os.path.abspath(os.path.join(MARKDOWN_DIR, filename))

    # Confirm the file is within the markdown dir
    if not source_file.startswith(os.path.abspath(MARKDOWN_DIR)):
        return abort(403)  # Prevent directory traversal

    if request.method == "POST":
        with open(source_file, "w", encoding="utf-8") as f:
            f.write(request.form["content"])
        subprocess.run(["mkdocs", "build"], cwd=BASE_DIR, check=True)
        return '<div id="status">Saved!</div>'

    if not os.path.exists(source_file):
        return "File not found", 404

    with open(source_file, "r", encoding="utf-8") as f:
        content = f.read()

    return render_template("editor.html", content=content, note_name=filename)


if __name__ == "__main__":
    app.run(debug=True, port=5007)
