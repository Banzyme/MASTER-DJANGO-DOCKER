 #! /bin/bash
 
 # Start a new django project using docker
 projectName="twisted"
 echo $projectName
 docker-compose run web django-admin.py startproject $projectName .
# Change file ownership to current user since docker runs as root
 chown -R $USER:$USER .

 # Ask user if postgres database settings have been updated
echo -n "Done setting up postgres (y/n)? "
read answer
if [[ "$answer"=="y" || "$answer"=="Y" ]] ;then
    docker-compose up
    netstat -lnp | grep 5000
      
else
    echo "Please set-up postgres then run,docker-compose up"
    exit
fi

