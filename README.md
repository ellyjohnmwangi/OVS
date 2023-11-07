# OVS Online Votting System

OVS Is an online votting system crafted for campus students in Kenya.


## Instalation
### Get the files
1. From your terminal or cmd:
> git clone git clone https://github.com/ellyjohnmwangi/OVS.git

2. cd into the ovs directory
> cd OVS

3. Install requirements
Install a required packages
> pip install -r requirements.txt

### Install the DB
 cd into https://github.com/ellyjohnmwangi/OVS/database and import student_db2.sql into your mysql/mariadb server. If on testing environment use migrations.sql as it contains dummy data.
### Running
Run the main file
> python3 main.py

### Errors


## Directory Structure
0. main.py
    Main  file running the server an initializing everything
1. database
    database.sql import this to create your DB tables
    migrations.sql an import containing migration/random data for testing the DB
2. handlers
    Contains all the logic for serving .html files
3. modules
    Contains all back end logic for connecting to the DB for reading or writing into the DB
4. static
    Contains all static files like css, images or javascript files.
5. templates
    Contains all .html files to be served by the handlers.
6. tests
    Contains files describing  the unit tests.
7. utils
    Contains helpers functions to be used all through various libraries.

## Contribution
* Be sure to look at the directory structure to get an over view of project files*
1. Git clone  ovs
2. Work on your changes.
3. Create your own branch and add a PR to it. *Please add your commit message as per the changes you have made ie "Added user methods.", "Added voter tallying"*
4. Abstract your code away keeping CI in mind.
5. Update the readme directory description for added files.

*If you have added new pip packages, please initalize it for us with pip freeze*
> pip freeze > requirements.txt


##### ADIOS














## WHY's
*Add yours, potential exam questions*
Why does each handler do it's own db connection and not at the top of class initialization?
  in the case of two requests intiating the same db connection and one completing faster than the other then clossiing the connection hence the other probably won't get the results.

What happens when creating an Election:
  1. A term is created.
  2. Students get a chance to apply for various positions and the PO will select those who do qualify.

How does voting occur
  1. On server start up, it is checked to ensure if votting is on and initialised for the router
*Positions are created once during server initialization, this has a disadvantage of flexibility hence future implementations canm have admin functionality to create or delete various positions*
