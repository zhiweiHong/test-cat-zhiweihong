from setuptools import setup, find_packages

setup(
    name='cat',
    version='1.0.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'cat = cat.cat:meow'
        ]
    },
    description='A simple Python package that provides functionalities related to cats.',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/cat',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
