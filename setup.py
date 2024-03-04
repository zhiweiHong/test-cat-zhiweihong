from setuptools import setup, find_packages

setup(
    name='test-cat-zhiweiHong',
    version='2.0.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'cat = cat.cat:meow'
        ]
    },
    description='A simple Python package that provides functionalities related to cats.',
    author='zhiweiHong',
    author_email='970060150@qq.com',
    url='https://github.com/zhiweiHong/test-cat-zhiweihong',
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
