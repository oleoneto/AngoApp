#!/bin/bash
shopt -s expand_aliases
source ~/.bash_profile

# Written by Leo N.
# Created on: October 23, 2017
# Updated on: February 23, 2018
# Ekletik Studios

# Using the following configuration:
SITE="AngoApp"
MEDIA_REPO="AngoApp"
DOMAIN="angoapp.com"
MEDIA_SERVER="_media"
STATIC_SERVER="_static"

# Enter repository
cd ~/$SITE
echo "Working from inside $PWD"

# Update the repository
git pull origin

# Collect all static files
workon $SITE
./manage.py collectstatic
# If errors occur, run: python manage.py collectstatic

# Deactivating the virtual environment
deactivate
echo "Virtual environment deactivated."

# Copy media files...
if [ "$MEDIA_REPO" ]
then
    if [ "$DOMAIN" ]
    then
        if [ "$MEDIA_SERVER" ]
        then
            echo "Copying files from $MEDIA_REPO to $DOMAIN/$MEDIA_SERVER"
            cp ~/$SITE/$MEDIA_REPO/ /var/www/$DOMAIN/$MEDIA_SERVER/
        fi
          echo "Files copied."
    fi
fi

if [ !"$MEDIA_SERVER" ]
then
    echo "Files NOT copied."
fi


# Once all files have been copied, this restarts the nginx and the wsgi servers.
service nginx restart
service uwsgi restart
echo "NGINX and WSGI restarted."

# eof
