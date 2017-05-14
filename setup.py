from setuptools import setup, find_packages

setup(
    name='tomopyui',
    version='0.1',
    author='Francesco De Carlo',
    author_email='decarlof@gmail.com',
    packages=find_packages(),
    package_data={'':['tomopy.ui', 'fileDX.ui']},
    scripts=['bin/tomopyui'],
    description='Basic GUI for tomopy',
    install_requires=['pyqtgraph'],
    zip_safe=False,
)

