#!/usr/bin/env bash

mkdocs build
.venv/bin/python to_pdf.py
#mkdocs gh-deploy
git add .
git commit -m "update"
git push
rsync -av ./site/ tyler@192.168.1.104:/srv/web_apps/notes/