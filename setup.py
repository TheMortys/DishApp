from setuptools import setup, find_packages

setup(
    name='dishHelper',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Package to help with dishes for guests',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/TheMortys/DishApp',
    author='Marek Morys',
    author_email='example@mail.com',
    package_data={'packageData': ['myData.dat']},
    include_package_data=True
)