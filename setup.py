from setuptools import setup, find_packages

setup(
    name='fut-card-creator',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'certifi==2018.11.29',
        'chardet==3.0.4',
        'idna==2.8',
        'oauthlib==3.0.0',
        'PySocks==1.6.8',
        'requests==2.21.0',
        'requests-oauthlib==1.2.0',
        'six==1.12.0',
        'tweepy==3.7.0',
        'urllib3==1.24.1',
    ],
    include_package_data=True,
    description='FUT Card Creator package',
    author='Ilyas Mohamed',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/fut-card-creator',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
