#!/usr/pkg/bin/python2.7


import csv
from subprocess import Popen, PIPE

fname = "Export_LP.csv"
file = open(fname, "rb")

def path_for(element, path=None):
	""" Generate path name from elements name and current path """
	path = "%s/%s" % (element[5], element[4]) 
	return path

def password_data(element):
	URL = "URL: " + element[0]
	ID = "ID: "+ element[1]
	pw = "Password: " + element[2]
	data = "%s\n%s\n%s" % (URL,ID, pw)
	return data

def import_entry(element, path=''):
    """ Import new password entry to password-store using pass insert
    command """
    print "Importing " + path_for(element, path)
    proc = Popen(['pass', 'insert', '--multiline', '--force',
                  path_for(element, path)],
              stdin=PIPE, stdout=PIPE)
    proc.communicate(password_data(element).encode('utf8'))
    proc.wait()

try:
	reader = csv.reader(file)
	for row in reader:
		import_entry(row)
finally:
	file.close()
