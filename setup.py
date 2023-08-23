from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'


def get_requirements(file_path):
    '''
    This function will return the list of all the required libraries
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name = "Ml-Project",
    version = '0.0.1',
    author= 'Madhuranjan Kumar',
    author_email='madhuranjan763@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)