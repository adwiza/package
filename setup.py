from setuptools import find_packages, setup


def read_requirements_txt():
    with open('requirements.txt') as fp:
        requirements = [line.strip() for line in fp]
    return requirements


setup(
    name='mycalc',
    version='0.0.1',
    description='A small example package with some arithmetics',
    packages=find_packages(),
    install_requires=read_requirements_txt(),
    include_package_data=True,
    author='Amazing Author',
    author_email='author@example.com',
    url='https://github.com/adwiza/package.git',
)
