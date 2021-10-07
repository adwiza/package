from setuptools import find_packages, setup

setup(
    name='mycalc',
    version='0.0.1',
    description='A small example package with some arithmetics',
    packages=find_packages(),
    include_package_data=True,
    install_requires='',
    author='Amazing Author',
    author_email='author@example.com',
    url='https://github.com/adwiza/package.git',
)
