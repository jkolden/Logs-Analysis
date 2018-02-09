# Logs-Analysis
Logs Analysis Project for Udacity Full Stack Nanodegree.

This project uses psycopg2 to query a mock PostgreSQL database for a fictional news website. The questions answered by this program are:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

The database that this program queries contains three tables: articles, authors and log. The definitions of these tables is as follows:

### articles table definition:
author | integer                  | not null
title  | text                     | not null
slug   | text                     | not null
lead   | text                     |
body   | text                     |
time   | timestamp with time zone | default now()
id     | integer                  | not null default nextval('articles_id_seq'::regclass)

### authors table definition:
name   | text    | not null
bio    | text    |
id     | integer | not null default nextval('authors_id_seq'::regclass)

### log table definition
path   | text                     |
ip     | inet                     |
method | text                     |
status | text                     |
time   | timestamp with time zone | default now()
id     | integer                  | not null default nextval('log_id_seq'::regclass)

## How to run this code

### Install the VM and Vagrant:
This project uses a virtual machine (VM) to run a SQL database server.
1. If you don't already have virtual box on your machine, you can download it here:
- https://www.virtualbox.org/wiki/Download_Old_Builds_5_1
2. Download and install Vagrant (if you do not already have it installed). This is the software that configures the VM and allows the host (your machine) to talk to the VM:
- https://www.vagrantup.com/downloads.html
- you should be able to run ```$ vagrant --version``` after installation to see the version that was installed.
3. Clone this repository: https://github.com/udacity/fullstack-nanodegree-vm to a directory on your local machine and then cd into this directory.
4. cd into the vagrant/ subdirectory
5. Bring the VM up with the command ```vagrant up```
6. Log into the VM with ```vagrant ssh```

### Download the news data and run the commands to populate the database:
1. Download the news data from here:
- https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
2. Unzip this file and move the newsdata.sql file into your vagrant directory
3. cd into the vagrant directory and run ```psql -d news -f newsdata.sql```
- This will connect to the news database and populate the tables with the data contained in the sql file.

### Download and run the news.py file
1. Clone this repository to your local drive: https://github.com/jkolden/Logs-Analysis
2. Copy the news.py file into the fullstack-nanodegree-vm/vagrant directory.
3. Open a terminal window from the fullstack-nanodegree-vm/vagrant directory, or simply open a terminal window and cd into that directory.
4. Run vagrant ssh at the prompt to log in to the VM.
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
