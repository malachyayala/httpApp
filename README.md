<h2> Overview </h2>
An animation represents objects moving and changing its state in a series of ticks.

A simple version of our model is created with the length and width frame the animation will take place in.

Several versions of our view are created by providing a model with shapes and commands.

Step #1:
Make sure you have some version of python installed that is at least 3.7.9. If you do not have this, follow this: https://realpython.com/installing-python/ guide to do so.

Step #2:
If you already have some version of python installed that is at least 3.7.9, the next step is to make you have pip installed and if not, to download it. After downloading python, pip should already be installed on your machine but to check run the command: 'pip -V'. If it returns a version, pip is installed. If pip has not been installed, follow this: https://pip.pypa.io/en/stable/installation/ tutorial to install it.

Step #3:
Once pip installed, run 'pip3 install Django' in your terminal.

Step #4:
After installing Django, navigate to wherever you stored the httpApp/ directory.

Step #5:
Once in the httpApp/ directory, run the following command in your terminal: 'python3 manage.py runserver'. The HTTP API should now be ready for testing.

For testing:

brew install mysql
brew install openssl
export PATH=${PATH}:/usr/local/mysql/bin/
sudo xcode-select --reset
pip3 install mysqlclient

python3 manage.py makemigrations
python3 manage.py migrate

mysql -u root -p

SHOW DATABASES;
CREATE DATABASE my_db;
