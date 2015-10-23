from setuptools import find_packages
from setuptools import setup


setup(
    name='pre_commit_hooks',
    description='ruby -wc pre commit hook.',
    url='https://github.com/therealjessesanford/rubywc-pre-commit-hook',
    version='0.1',

    author='Jesse Sanford',
    author_email='jessesanford@gmail.com',

    packages=find_packages('.', exclude=('tests*', 'testing*')),

    entry_points={
        'console_scripts': [
            'check-rubywc = pre_commit_hooks.check_rubywc:check_rubywc',
        ],
    },
)
