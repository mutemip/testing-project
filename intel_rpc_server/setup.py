from setuptools import setup, find_packages

setup(
    name='intel_rpc',
    version='0.0.1',
    description='Trusted intel client/server generated grpc files',
    author='Michael Tetteh',
    author_email='mike@panabios.org',
    url='https://github.com/Koldchain1/Trusted_Intel_Platform_Backend',
    packages=find_packages(include=['intel_rpc']),
    install_requires=[
      'grpcio==1.41.1'
    ],
)