from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

with open('requirements.txt', 'r') as f:
    requirements = f.read().splitlines()

setup(
    name='json_morph',
    version='1.0.0',
    description="A Python tool for converting and manipulating data between JSON and various formats.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Mahdi Pourgholami',
    url='https://github.com/Medix13/json_morph.git',
    packages=find_packages(),
    install_requires=requirements,
    entry_points='''
        [console_scripts]
        JSONMorph=JSONMorph.JSONMorph:main
    ''',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
