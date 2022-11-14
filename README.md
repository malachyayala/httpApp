<h2> Setting up enviorment </h2>
<h3>Step #1:</h3>
Make sure you have some version of python installed that is at least 3.7.9. If you do not have this, follow this: https://realpython.com/installing-python/ guide to do so.

<h3>Step #2:</h3>
If you already have some version of python installed that is at least 3.7.9, the next step is to make you have pip installed and if not, to download it. After downloading python, pip should already be installed on your machine but to check run the command: 'pip -V'. If it returns a version, pip is installed. If pip has not been installed, follow this: https://pip.pypa.io/en/stable/installation/ tutorial to install it.

<h3>Step #3:</h3>
Once pip installed, run 'pip3 install Django' in your terminal.

<h3>Step #4:</h3>
Next, you must install MySql. Follow this: https://pypi.org/project/mysqlclient/ guide depending on which OS you have. Personally, I have macOS and ran into some issues installing MySql. These are the commands I eventually ran to make it run:
- brew install mysql  
- brew install openssl  
- export PATH=${PATH}:/usr/local/mysql/bin/   
- sudo xcode-select --reset  
- pip3 install mysqlclient  


<h3>Step #5:</h3>
After installing Django, navigate to wherever you stored the httpApp/ directory.

Step #5:
Once in the httpApp/ directory, run the following command in your terminal: 'python3 manage.py runserver'. The HTTP API should now be ready for testing.

For testing:


python3 manage.py makemigrations
python3 manage.py migrate

mysql -u root -p

SHOW DATABASES;
CREATE DATABASE my_db;
