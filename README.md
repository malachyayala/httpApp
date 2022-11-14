<h2> Setting up enviorment </h2>
<h3>Step #1:</h3>
Make sure you have some version of python installed that is at least 3.7.9. If you do not have this, follow this: https://realpython.com/installing-python/ guide to do so.

<h3>Step #2:</h3>
If you already have some version of python installed that is at least 3.7.9, the next step is to make you have pip installed and if not, to download it. After downloading python, pip should already be installed on your machine but to check run the command: 'pip -V'. If it returns a version, pip is installed. If pip has not been installed, follow this: https://pip.pypa.io/en/stable/installation/ tutorial to install it.

<h3>Step #3:</h3>
Once pip installed, run 'pip3 install Django' in your terminal.

<h3>Step #4:</h3>
Next, you must install MySql. Follow this: https://pypi.org/project/mysqlclient/ guide depending on which OS you have. Personally, I have macOS and ran into some issues installing MySql. These are the commands I eventually ran to make it run: <br />
- brew install mysql<br />
- brew install openssl<br />
- export PATH=${PATH}:/usr/local/mysql/bin/<br />
- sudo xcode-select --reset<br />
- pip3 install mysqlclient<br />

<h3>Step #5:</h3>
Once MySql is installed, you must create the database being used. This takes 3 commands. First, connect to MySql with 'sudo mysql.' This should take you to the MySql command-line client. If it does not work and requires a password, run 'mysql -u root -p' and enter your MySql password. However, The default should be no  password or an empty password.<br />
<br />
Once in the MySql client, enter 'SHOW DATABASES;' to see what databases already exist. If there is no 'my_db', run 'CREATE DATABASE my_db;'. 

<h2> Running API </h2>
<h3>Step #1:</h3>
After installing Django and MySql, navigate to wherever you stored the httpApp/ directory.

<h3>Step #2:</h3>
Once in the httpApp/ directory, run the following commands in your terminal:<br />
- python3 manage.py makemigrations<br />
- python3 manage.py migrate<br />

This should migrate Django and the newly created MySql db.

<h3>Step #3:</h3>
In order to start and run the program, run the follow command: 'python3 manage.py runserver'. The HTTP API should now be ready for testing.

<h2> Testing </h2>
In order to test the API, I have provided some commands to test functionality:

<h4>Add a team member: </h4>
curl -X POST -H "Content-Type:application/json" http://127.0.0.1:9000/users -d '{"userId": 1, "firstName": "Malachy", "lastName": "Skywalker", "phone": "+12345678900", "emailId": "inagalaxy@farfaraway.com", "role": 0}'

<h4>List team members:</h4>
curl -X GET http://127.0.0.1:8000/users/

<h4>Delete a team member:</h4>
curl -X DELETE -H "Content-Type:application/json" http://127.0.0.1:8000/users/ -d '{"userId": 1}'

<h4>Update a team member:</h4>
curl -X PUT -H "Content-Type:application/json" http://127.0.0.1:8000/users/ -d '{"userId": 1, "emailId": "hello@test.com", "role": "admin"}'
