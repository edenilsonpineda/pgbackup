from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='pgbackup-py',
    version='0.1.0',
    author='Edenilson Pineda',
    author_email='edenilsonpineda@outlook.com',
    description='A utility for backing up PostgresSQL databases and save it locally or on a bucket',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/edenilsonpineda/pgbackup-py',
    packages=find_packages('src')
)
