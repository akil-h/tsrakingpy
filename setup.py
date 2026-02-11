from setuptools import find_packages, setup

setup(
    name='tsraking',
    packages=find_packages(include=['tsrakingpy']),
    description='Python library with scripts to balance time series data.',
    author='Akil Huang',
    install_requires=['numpy'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)