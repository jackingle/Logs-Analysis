# Log Analysis Reporting Tool

This python based program is a reporting tool created to analyze a mock database
for a Udacity nanodegree project.  The psycopg2 module enables the python class
to communicate with a Postgresql database and perform queries.  

This database contains newspaper articles, information about the authors, and
log information.  The log information is most important as it enables the
reporting tool to gleam meaningful information regarding access frequency.  

## Installation

This project required a virtual machine with a premade database but not  all of
the listed dependencies may be required.  For safety's sake, I have included
all of the dependencies I had.

- Python 2 or 3(any version)
- PostgreSQL 9.6
- Vagrant
- VirtualBox
- newsdata.sql database

newsdata.sql database can be found within newsdata.zip [at this link](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).
The necessary virtual machine can be found [at this link](https://github.com/udacity/fullstack-nanodegree-vm/blob/master/vagrant/Vagrantfile).
Install Vagrant from [here](https://www.vagrantup.com/downloads.html).
Install ViritualBox from [here](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1).

### Start the virtual machine

You will need some form of Unix shell in order to execute commands to log in to
the virtual machine.  After you have installed the dependencies, use the
following commands.  
```
cd /vagrant/
vagrant up
vagrant ssh
```

### Load the newsdata into the database

While in the vagrant directory of the virtual machine, use the following command.  This will update the PostgreSQL database with the mock information.
```
psql -d news -f newsdata.sql
```

### Run the Log Analysis Reporting Tool

Place the file logs.py in the shared folder for the virtual machine. The example
code below shows python3 being used but this program will work in python2 as
well.
```
python3 logs.py
```

### Review the output

The code executes the queries and provides both questions and answers in the
output.  This code will return in the same program utilized to compile the
python code, such as Git Bash for example.
