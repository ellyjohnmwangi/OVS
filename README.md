# OVS Online Votting System

OVS Is an online votting system crafted for campus students in Kenya.


## Instalation
### Get the files
1. From your terminal or cmd:
> git clone git clone https://github.com/ellyjohnmwangi/OVS.git

2. cd into the ovs directory
> cd OVS

3. Install requirements
*Might ad this later if necessary but for now we assume not*

### Install the DB
 cd into https://github.com/ellyjohnmwangi/OVS/db and import student_db2.sql into your mysql/mariadb server. If on testing environment use migrations.sql as it contains dummy data.
### Running
Run the main file
> python3 main.py

### Errors


## Directory Structure
1. Data: Stores all logs(error logs and request logs) and data for internal use case
      logs: Contains all logged out errors
      config: Contains the configuration file for connecting to DB *Might change to use environment variables*
2. DB: student_db2.sql Describes the database structure for production environment.
       migrations.sql Is a dump for testing the DB, import it to your test DB if necessary.
3. main.py Entrypoint for running the whole project
4. modules FIles containing classes and project code.
    DB Connections are made whhen necessary that way we dont need a db connection pool or a thread to manage db connections.

## Contribution
* Be sure to look at the directory structure to get an over view of project files*
1. Git clone  ovs
2. Work on your changes.
3. Create your own branch and add a PR to it. *Please add your commit message as per the changes you have made ie "Added user methods.", "Added voter tallying"*
4. Abstract your code away keeping CI in mind.
5. Update the readme directory description for added files.

##### ADIOS
