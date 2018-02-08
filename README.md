# Logs-Analysis
Logs Analysis Project for Udacity Full Stack Nanodegree

###  Required Views
Before running this code, create the following view:
```
create view log_v as select substr(path, 10) title, ip, method, status, time, id from log;
```
### How to run this code
1. Assuming you have the VM installed, find the fullstack-nanodegree-vm folder in your local directory and then find the vagrant folder within that directory and open a terminal window.
2. Run vagrant ssh at the prompt to connect to the VM.
```
$ vagrant ssh
```
3. cd into the vagrant subdirectory
```
vagrant@vagrant:~$ cd /vagrant
```
4. Run the news.py program
```
vagrant@vagrant:/vagrant$ python news.py
```
5. The program's output will be displayed in the terminal window.

