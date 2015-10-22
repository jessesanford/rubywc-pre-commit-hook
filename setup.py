from setuptools import find_packages
from setuptools import setup


setup(
    name='pre_commit_hooks',
    description='reek pre commit hook.',
    url='https://github.com/therealjessesanford/reek-pre-commit-hook',
    version='0.1',

    author='Jesse Sanford',
    author_email='jessesanford@gmail.com',

    packages=find_packages('.', exclude=('tests*', 'testing*')),

    entry_points={
        'console_scripts': [
            'check-reek = pre_commit_hooks.check_reek:check_reek',
        ],
    },
)
