#!/usr/bin/env bash

mkdocs gh-deploy
git add .
git commit -m "update"
git push
