from setuptools import setup

version = '0.1.0'

setup(
    name='shh',
    version=version,
    url='https://github.com/wybiral/shh/',
    author='Davy Wybiral',
    author_email='davy.wybiral@gmail.com',
    description='Making Tor hidden services easy',
    packages=['shh'],
    platforms='any',
    install_requires=[
        'stem==1.4.0',
    ],
    classifiers=[
    ],
)