from setuptools import find_packages,setup
from typing import List


HYPHEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    requiremests = []
    with open(file_path) as file_obj:
        requiremests = file_obj.readlines()
        requirements = [ req.replace('\n','') for req in requiremests] 
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
            
            
    return requirements

setup(name= 'Zomato_Delivery',
      version= '0.0.1',
      author= 'Kartikay Garg',
      author_email= 'kartikaygarg282@gmail.com',
      install_requires = get_requirements('requirements.txt'),
      packages= find_packages()
)






