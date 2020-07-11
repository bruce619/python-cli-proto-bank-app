from setuptools import setup


setup(
    name='protobankapp',
    version='0.1.0',
    packages=['protobankapp'],
    entry_points={
        'console_scripts': [
            'protobankapp = protobankapp.__main__:main'
        ]
    })

