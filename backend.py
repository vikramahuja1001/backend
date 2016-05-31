import os

from dulwich import porcelain as p
from dulwich.repo import Repo as DulwichRepo
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
		self.activity = ""
		self.repo_path = ""
		self.repo_name = ""


	def set_authorinfo(self, username, email):
		self.username = username
		self.email = email


	def local_init(self, repo_name, activity):
		self.activity = activity
		self.repo_name = repo_name
		try:
			self.repo = p.init(repo_name)
			self.current_dir = os.getcwd()
			self.repo_path = self.current_dir + '/' + self.repo_name
			print self.repo_path
			print "Local Repo Created"
		except:
			print "Repo already exist, delete it first"

	def load_repo(self, repo_name):
		self.repo_name = repo_name
		self.repo = DulwichRepo(self.repo_name)
		self.current_dir = os.getcwd()
		self.repo_path = self.current_dir + '/' + self.repo_name


	def create_file(self, name, content):
		try:
			file = open(os.path.join(self.repo_path,name), 'w')
			file.write(content)
			file.close()
		except:
			print 'Unable to create README, does it already exist?'


	def edit_readme(self, name, content):
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
			print self.repo_path
			print p.status(self.repo_path)
		else:
			print "Repo does not exist"


	def commit(self, message):
		p.commit(self.repo, message)


	def get_commit_history(self):
		print self.repo_path
		r = self.repo
		p = "README"
		w = r.get_walker(paths=[p], max_entries=None)
		count = 0
		for i in iter(w):
			count += 1
			print count,
			print i
			print i.commit


	def clone_local(self,clone_repo_name):
		#Creating a clone of a given repo. The repo should be local.
		p.clone(self.repo_path,clone_repo_name)


	def clone_remote(remote_repo_name, clone_repo_name):
		#Creating a clone of remote repo.
		p.clone(remote_repo_name, clone_repo_name)


	def commit_logs(self):
		try:
			if os.path.exists(self.repo_path):
				print p.log(self.repo)
			else:
				print "Repo does not exist"
		except:
			print "No commits yet"


	def go_to_commit(self):
		print self.repo_path
		r = self.repo
		p = "README"
		w = r.get_walker(paths=[p], max_entries=None)
		count = 0
		for i in iter(w):
			count += 1
			print count,
			print i
			print i.commit.get_sha_for()
		p.reset(self.repo, "hard", )



	#def push():

	#def pull():

	#def clone():



