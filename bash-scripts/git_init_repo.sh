#! /bin/bash

git_url = "https://github.com/Banzyme/"
git_ext = ".git"
input_repo_name = "$1"
new_repo_name = "$input_repo_name$git_ext"

touch README.md
chown -R $USER:$USER .
git init
git add . &&\
git commit -m "first commit" &&\
git remote add origin "https://github.com/Banzyme/MASTER-DJANGO-DOCKER.git" &&\
git push -u origin master