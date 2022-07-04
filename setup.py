from setuptools import setup, find_packages

setup(
    name='panabios_rpc',
    version='0.0.1',
    description='panabios client/server generated grpc files',
    author='Michael Tetteh',
    author_email='mike@panabios.org',
    url='https://github.com/Koldchain1/Koldchain_App_Backend/',
    packages=find_packages(include=['panabios_rpc', 'lab_test_proto']),
    install_requires=[
      'grpcio==1.41.1'
    ],
)