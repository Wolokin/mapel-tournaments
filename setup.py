import os
import setuptools
from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()
    
mapel_dir_1 = os.path.join('controllers','models')
mapel_dir_2 = os.path.join('results','points')

setup(name='map-of-elections',
      version='1.0.5',
      description='Map of Elections',
      url='https://github.com/szufix/mapel',      
      download_url='https://github.com/szufix/mapel/archive/v1.0.5.tar.gz',
      author='Stanislaw Szufa',
      author_email='s.szufa@gmail.com',
      package_data={'mapel': [mapel_dir_1 + '/*.txt', mapel_dir_2 + '/*.txt']},
      packages=setuptools.find_packages(),
      install_requires=['numpy'],
      zip_safe=False)
