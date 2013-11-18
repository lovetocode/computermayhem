try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup
	
config = {
	'description': 'My Project',
	'author': 'My Name',
	'url': 'URL to get it at.'.
	'download_url': 'Whre to download it',
	'author_email': 'My email',
	'Version': '0.1',
	'install_requires': ['nose'],
	'packages': ['NAME'],
	'scripts': [],
	'name': 'projectname'
	
}

setup(**config)
	