## Datajoint pipelines and code for the Hillman lab (SCAPE Team).

# Install docker and datajoint 
1. Install Docker and Docker compose: Docker: https://docs.docker.com/get-docker/ Docker compose: Docker in Mac and Windows comes with Compose. For Linux, you will need to install Compose separately: https://docs.docker.com/compose/install/

2. Fork the repository (https://github.com/hillmanlab/datajoint-hillman-SCAPE.git) onto your own GitHub account by clicking on the 'Fork' button in the top right corner of Github.

3. Clone the forked repository, i.e. copy the files to your local machine by `git clone https://github.com:YourUserName/datajoint-hillman-SCAPE.git`. Important: do *not* clone the repo from `hillmanlab`, but the one that you forked onto your own account!

4. Now let's start to setup the docker environment. Create a folder that you want to store the database. The files that customize the settings are `Dockerfile` and `docker-compose.yml`, so copy these files to the folder that you just created. Finally, run 'docker-compose up -d' or 'sudo docker-compose up -d' depending on the OS to start the MySQL server in the terminal.
After it is finished, you could check the status of the docker container by docker ps.

