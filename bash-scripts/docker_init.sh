 #! /bin/bash
 
 # Start a new django project using docker
 project_name = "twisted"
 docker-compose run web django-admin.py startproject $project_name .
# Change file ownership to current user since docker runs as root
 chown -R $USER:$USER .

 # Ask user if postgres database settings have been updated
echo -n "Done setting up postgres (y/n)? "
read answer
if [[ "$answer"=="y" || "$answer"=="Y" ]] ;then
    docker-compose up
else
    echo "Please set-up postgres then run,docker-compose up "
    exit
fi

