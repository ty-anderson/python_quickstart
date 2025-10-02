#!/usr/bin/env bash

mkdocs build
#.venv/bin/python to_pdf.py
# mkdocs gh-deploy
git add .
git commit -m "update"
#git push origin master
git push backup master
rsync -av --delete --rsync-path="sudo rsync" ./site/ tyler@192.168.1.104:/srv/web_apps/notes/

# public version
mv mkdocs.yml mkdocs_original.yml
mv mkdocs_public.yml mkdocs.yml
mkdocs build
rsync -av --delete --rsync-path="sudo rsync" ./site/ tyler@192.168.1.104:/srv/web_apps/public_notes/
mv mkdocs.yml mkdocs_public.yml
mv mkdocs_original.yml mkdocs.yml