from importlib.metadata import entry_points
from setuptools import find_packages, setup


setup(name='clean_folder',
      version='2.0',
      description='Script that sorts files in a folder into categories',
      author='Serhii Borodin',
      author_email='bsy.prog@gmail.com',
      license='MIT',
      entry_points={
        'console_scripts': ['clean-folder=clean_folder.clean:main']
      },
      packages=find_packages())
