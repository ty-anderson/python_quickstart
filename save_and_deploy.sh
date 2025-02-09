#!/usr/bin/env bash

mkdocs gh-deploy
git commit -m "update"
git push
