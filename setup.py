from setuptools import setup, find_packages

setup(name="autosmoke",
        version="0.0.0",
        url="https://github.com/dongik/autosmoke",
        license="MIT",
        author="Dongik Lee",
        author_email="dongik2.lee@gmail.com",
        description="Test automation",
        packages=find_packages(exclude=['tests']),
        long_description=open('README.md').read(),
        zip_safe=False)

