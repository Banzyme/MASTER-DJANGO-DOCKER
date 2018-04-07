#! /bin/bash

echo "Preparing to push to origin"
git add . &&\

echo "Add successful" &&\

git commit -m "$1" &&\

echo "Completed!" &&\

git push &&\

echo "Push to remote completed."