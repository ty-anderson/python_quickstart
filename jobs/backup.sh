#!/usr/bin/env bash

rsync -avz --rsync-path="sudo rsync" /Users/tyleranderson/tmp/ tyler@anderson.home:/home/tyler/.backup/tmp
echo "Ran on $(date +%Y-%m-%d--%H:%M:%S)" >> logs/backup.log
