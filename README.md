# Logs-Analysis
Logs Analysis Project for Udacity Full Stack Nanodegree

###  Required Views
Before running this code, create the following view:
```
create view log_v as select substr(path, 10) title, ip, method, status, time, id from log;
```
### How to run this code
1. Clone this repository to your local drive.
2. Assuming you have the VM installed, copy the news.py file into the fullstack-nanodegree-vm/vagrant directory.
3. Open a terminal window from the fullstack-nanodegree-vm/vagrant directory, or simply open a terminal window and cd into that directory.
4. Run vagrant ssh at the prompt to connect to the VM.
```
$ vagrant ssh
```
5. cd into the vagrant subdirectory
```
vagrant@vagrant:~$ cd /vagrant
```
6. Run the news.py program
```
vagrant@vagrant:/vagrant$ python news.py
```
7. The program's output will be displayed in the terminal window.
