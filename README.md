## Datajoint pipelines and code for the Hillman lab (SCAPE Team).

# Install docker and datajoint 
1. Install Docker and Docker compose: Docker: https://docs.docker.com/get-docker/ Docker compose: Docker in Mac and Windows comes with Compose. For Linux, you will need to install Compose separately: https://docs.docker.com/compose/install/
2. Fork the repository (https://github.com/hillmanlab/datajoint-hillman-SCAPE.git) onto your own GitHub account by clicking on the 'Fork' button in the top right corner of Github.
3. Clone the forked repository, i.e. copy the files to your local machine by `git clone https://github.com:YourUserName/datajoint-hillman-SCAPE.git`. Important: do *not* clone the repo from `hillmanlab`, but the one that you forked onto your own account!
4. Now let's start to setup the docker environment. Create a folder that you want to store the database. The files that customize the settings are `Dockerfile` and `docker-compose.yml`, so copy these files to the folder that you just created. Finally, run 'docker-compose up -d' or 'sudo docker-compose up -d' depending on the OS to start the MySQL server in the terminal.
After it is finished, you could check the status of the docker container by docker ps.
5. Install git and datajoint. For Anaconda, run the following commands in prompt (Admin)
   conda install git
   pip install datajoint
   

# Install and setup Datajoint on Matlab
To run the packages yourself, you will need to install DataJoint matlab and have access to a database server.
To install DJ matlab:
1.	Click Add-Ons on Matlab homepage.
2.	Select Get Add-Ons
3.	Search for datajoint
4.	Click on DataJoint icon
5.	Click install from GitHub



# Use Python defined pipeline in Matlab
1. Use dj.createSchema and let it walk you through creating the package.
+ Provide the existing schema name (e.g. hillman_subject).
+ Follow the instruction and create a MATLAB package (a folder that begins with a +, e.g. +subject)
The package need to be created only once. After that, the user can get the schema via getSchema command.
+ You will be able to plot the schema diagram at the point, such as erd subject
2. If you just want to access the data and do some queries and fetches, you could just do:
>> schema = subject.getSchema
>> schema.v.Subject
3. If you need to recover the class for a particular table, do dj.new , the table name should be the one existing in the database. Then the definition will be reverse engineered in the .m script.
