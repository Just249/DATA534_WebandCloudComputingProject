from setuptools import setup, find_packages

setup(
    name='gcdpd-wrapper',
    version='1.0',
    packages=find_packages(exclude=['api_wrapper_test*']),
    license='MIT',
    description='Gov of Canada Drug Product Database API Wrapper',
    url='https://github.com/Just249/DATA534_WebandCloudComputingProject',
    author='Justin Chan, Kenny Tong, Vimaljeet Singh',
    author_email='cmtong1108@gmail.com'
)