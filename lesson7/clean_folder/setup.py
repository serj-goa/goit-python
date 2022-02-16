from setuptools import setup


setup(
    name='clean_folder',
    version='1',
    description='Sorting files in folder',
    url='https://github.com/serj-goa/goit-python/tree/main/lesson6',
    author='Serhii Borodin',
    author_email='bsy.prog@gmail.com',
    license='MIT',
    packages=['clean_folder'],
    entry_points={
        'console_scripts': ['clean-folder=clean_folder.clean:main']
    }
    )
