from setuptools import setup, find_packages

setup(
    name='ImgTiler',
    version='0.1.0',
    
    long_description='ImgTiler is a Python library for tiling and retiling images. It can be used for splitting large images into smaller tiles for other applications like Training Deep Learning models, inference on large images, etc.',
    author='Collins Wakholi',
    author_email='wcoln@yahoo.com',
    url='https://github.com/CollinsWakholi/ImgTiler',
    download_url = 'https://github.com/collinswakholi/ImgTiler/archive/refs/tags/v0.1.0.tar.gz',
    packages=find_packages(),
    install_requires=[
        'opencv-python',
        'numpy',
        'matplotlib',
    ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.11',
        'Operating System :: OS Independent',
    ],
)
