from setuptools import setup, find_packages
from pybase3 import __version__

setup(
    name='pybase3',
    version=__version__,
    description='A Python library to manipulate DBase III database files',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Domingo E. Savoretti',
    author_email='esavoretti@gmail.com',
    url='https://github.com/sandy98/pybase3',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'dbfview=pybase3.dbfview:main',
            'dbftest=pybase3.test:testdb',
            'pybase3=pybase3.__main__:main',
        ],
    },
    license='MIT',
    license_files=('LICENSE',),    
)