from backend import *
b = backend() 
print "Instance of backend created"
print b.activity
#n = input()
#print "0 : Exit\n1: Initialize a local repo\n2: Create a readme\n3:Adding the readme\n4: Editing readme\n5: Get status"
while 1:
	print "0 : Exit\n1: Initialize a local repo\n2: Create a readme\n3:Adding files(Add command)\n4: Editing readme\n5: Get status"
	n = input()
	if n == 0:
		break
	if n == 1:
		b.local_init("turtle")
		print "Local Repo Created"
	elif n == 2:
		b.create_readme_file()
		print "readme created"
		print b.repo_name
	elif n == 3:
		b.add("README")
	elif n == 4:
		b.edit_readme("Changing the readme")
	elif n == 5:
		b.get_status()
	elif n == 6:
		a = raw_input()
		b.commit(a)
	elif n ==7:
		b.get_previous_versions()


