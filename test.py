from backend import *
b = backend() 
print "Instance of backend created"
print b.activity
#n = input()
#print "0 : Exit\n1: Initialize a local repo\n2: Create a readme\n3:Adding the readme\n4: Editing readme\n5: Get status"
while 1:
	print "0 : Exit\n1: Initialize a local repo\n2: Create a readme\n3:Adding files(Add command)\n4: Editing readme\n5: Get status\n6: Commit\n7: Check Commit History\n8:Commit Logs\n9: Got to commit\n10:Load a git repo\n11: Diff tree(2 trees :P)"
	n = input()
	if n == 0:
		break
	if n == 1:
		b.local_init("turtle", "TurtleJS")
	elif n == 2:
		b.create_file("README","This is readme")
		print "readme created"
		print b.repo_name
	elif n == 3:
		b.add("README")
	elif n == 4:
		print "Enter new content of file to be changed:"
		a = raw_input()
		b.edit_readme("README", a)
	elif n == 5:
		b.get_status()
	elif n == 6:
		print "Enter Commit Message"
		a = raw_input()
		b.commit(a)
	elif n ==7:
		b.get_commit_history()
	elif n == 8:
		b.commit_logs()
	elif n ==9 :
		b.revert_to_commit()
	elif n == 10:
		b.load_repo("turtle")
		print "Loaded repo : turtle"
	elif n== 11:
		b.get_diff()


