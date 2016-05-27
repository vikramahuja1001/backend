import os

from dulwich import porcelain as p
from dulwich import repo
import time

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

	def edit_readme(self, content):
		name = "README"
		file = open(os.path.join(self.repo_path,name), 'w')
		file.write(content)
		file.close()

	def add(self, a):
		#a can be list of files or a single file
		print self.repo_name
		print self.repo
		if type(a) == list:
			for i in a:
				p.add(self.repo, i)
		else:
			p.add(self.repo, a)



	def get_status(self):
		if os.path.exists(self.repo_path):
			print p.status(self.repo_path)
		else:
			print "Repo does not exist"

	#def add_command(self,a = []):

	def commit(self, message):
		p.commit(self.repo, message)


	def get_previous_versions(self):
		print self.repo_path
		#r = Repo(".")
		r = self.repo
		print r
		p = "README"
		w = r.get_walker(paths=[p], max_entries=3)
		print iter(w)
		for i in iter(w):
			print "Vikram"
			print i.commit
		#try:
		#	c = iter(w).next().commit
		#except StopIteration:
		#	print "No file %s anywhere in history." % p
		#else:
		#	print "%s was last changed at %s by %s (commit %s)" % (
		#		p, time.ctime(c.author_time), c.author, c.id)

	#def push():

	#def pull():

	#def clone():



