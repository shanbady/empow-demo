# empow-demo
A demo dockerized api site for empow studios

# Usage
To get this running you must first have docker installed.

Once you have docker, you can start the app by running: `docker-compose up --build --detach`

Docker will initialize 3 containers:
1. An nginx container for serving static assets
2. The django web application
3. A postgres database instance


The docker compose also runs a django management script that creates some test posts and comments so we can test the functionality.

Once the the containers are running, you may visit http://localhost to see the running api server.


# Testing the "soft delete" functionality
To test a soft delete, login to the site as a superuser with the following credentials

username: root
password: password

Then navigate to a specific blog post in the api browser and hit "delete". You will note that the blog post no longer shows up anywhere on the api explorer. However, the blog post will still be accessible in django admin. Go to /admin and verify that that the post shows up in the admin browser.
You can also test this soft delete functionality with the post comments model.


There are also tests available under content/tests.py