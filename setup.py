from setuptools import setup

version = '0.9.0'

setup(
    name='shh',
    version=version,
    url='https://github.com/wybiral/shh/',
    author='Davy Wybiral',
    author_email='davy.wybiral@gmail.com',
    description='Making Tor hidden services easy',
    keywords = 'tor onion hidden service',
    packages=['shh'],
    platforms='any',
    install_requires=[
        'pysocks==1.6.7',
        'stem==1.5.4',
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Security',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
