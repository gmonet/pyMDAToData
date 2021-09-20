from setuptools import setup, find_packages

# https://blog.godatadriven.com/setup-py

setup(
    name='pyMDAToData',
    version='0.1.0',
    description='Better MDAnalaysis writer for DATA Lammps format file',
    author='Geoffrey Monet',
    packages=find_packages(),
    python_requires='>=3.6, <4',
    install_requires=[
        'numpy>=1',
        'MDAnalysis',
    ],
    include_package_data=True,
)
