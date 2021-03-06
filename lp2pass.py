#!/usr/pkg/bin/python2.7


import csv
import sys
from subprocess import Popen, PIPE

def path_for(element, path=None):
	""" Generate path name from elements name and current path """
	path = "{0}/{1}".format(element['grouping'], element['name']) 
	return path

def password_data(element):
	""" Extract data to fill each pass entry """
	URL = "URL: {0}".format(element['url'])
	ID = "ID: {0}".format(element['username'])
	pw = "Password: {0}".format(element['password'])
	data = "{0}\n{1}\n{2}".format(URL,ID, pw)
	return data

def import_entry(element, path=''):
    	""" Import new password entry to password-store using pass insert
    	command """
    	print "Importing {0}".format(path_for(element, path))
    	proc = Popen(['pass', 'insert', '--multiline', '--force',
                	path_for(element, path)],
              		stdin=PIPE, stdout=PIPE)
    	proc.communicate(password_data(element).encode('utf8'))
    	proc.wait()

def main(inputfile):
	file = open(inputfile, "rb")
	try:
		reader = csv.DictReader(file)
		imported = 0
		for row in reader:
			import_entry(row)
			imported = imported + 1
	finally:
		print "======================================"
		print "Imported {0} passwords into pass".format(imported)
		print "======================================"
		file.close()

if __name__ == "__main__":
	try:
		main(sys.argv[1])
	except IndexError:
		print "Please specify the name of the file to import"
		sys.exit(1)
