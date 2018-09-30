from setuptools import setup

setup(
    name='videoloop',
    version='0.1.0',
    packages=['videoloop'],
    entry_points={
        'console_scripts': [
            'videoloop = videoloop.__main__:main'
        ]
    })
