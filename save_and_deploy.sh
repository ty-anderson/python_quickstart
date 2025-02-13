#!/usr/bin/env bash

mkdocs build
mkdocs gh-deploy
git add .
git commit -m "update"
git push
scp -r ./site tyler@anderson.home:/srv/web_apps/notes