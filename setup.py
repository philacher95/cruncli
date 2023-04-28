from setuptools import setup, find_packages

setup(
	name='cruncli',
	version='0.0.0',
	packages=find_packages(),
	install_requires=[
		'click'
	],
	entry_points='''
	[console_scripts]
	crun=crun:crun
	'''
)