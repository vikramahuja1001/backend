import os

from dulwich import porcelain as p


"""Porcelain is a simple wrapper that provides porcelain-like functions on top of Dulwich.

Currently implemented functions in porcelain: 
 * archive
 * add
 * branch{_create,_delete,_list}
 * clone
 * commit
 * commit-tree
 * daemon
 * diff-tree
 * fetch
 * init
 * ls-remote
 * pull
 * push
 * rm
 * receive-pack
 * reset
 * rev-list
 * tag{_create,_delete,_list}
 * upload-pack
 * update-server-info
 * status
 * symbolic-ref

These functions are meant to behave similarly to the git subcommands.
Differences in behaviour are considered bugs.
"""

class backend():
	def __init__(self):
		self.username = ""
		self.email = ""
		self.activity = "TurtleJS"
		self.repo_path = ""
		self.repo_name = ""

	def set_authorinfo(self, username, email):
		self.username = username
		self.email = email

	def local_init(self, repo_name):
		self.repo_name = repo_name
		self.repo = p.init(repo_name)
		self.current_dir = os.getcwd()
		self.repo_path = self.current_dir + '/' + self.repo_name
		print self.repo_path

	def create_readme_file(self):
		name = "README"
		try:
			file = open(os.path.join(self.repo_path,name), 'w')
			file.write("This is a readme")
			file.close()
		except:
			print 'Unable to create README, does it already exist?'

	def add_readme(self):
		#Currently a variable will have to change to a file#
		print self.repo_name
		print self.repo
		p.add(self.repo, "README")
		print p.status(self.repo_path)




b = backend()
print b.activity
print b.email
b.local_init("turtle")
b.create_readme_file()
print b.repo_name
b.add_readme()










