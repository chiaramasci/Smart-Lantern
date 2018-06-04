#-*- coding: utf-8 -*-

import sqlite3

conn = sqlite3.connect('database.db')

print "Database creation successful"

#creation tables
conn.execute('CREATE TABLE DATA (ncard INT PRIMARY KEY NOT NULL, username TEXT NOT NULL, position INT NOT NULL, direction TEXT NOT NULL);')
conn.execute('CREATE TABLE START (ncard INT PRIMARY KEY NOT NULL, username TEXT NOT NULL);')
conn.execute('CREATE TABLE PATH (position INT PRIMARY KEY NOT NULL, direction TEXT NOT NULL);')

print "Data, Start and Path1 tables successfully created"
