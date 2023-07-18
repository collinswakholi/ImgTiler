from setuptools import setup, find_packages

with open('README.md', mode='r', encoding='utf-8') as fh:
    long_descr = fh.read()

with open("requirements.txt", "r") as f:
    req = f.readlines()

name_ = 'image_tiller'
desc_ = name_+' is a Python library for tiling and retiling images. It can be used for splitting large images into smaller tiles for other applications like Training Deep Learning models, inference on large images, etc.',
    
setup(
    name=name_,
    version='0.1.1',
    description=desc_,
    long_description=long_descr,
    long_description_content_type='text/markdown',
    author='Collins Wakholi',
    author_email='wcoln@yahoo.com',
    url='https://github.com/CollinsWakholi/ImgTiler',
    download_url='https://github.com/collinswakholi/ImgTiler/archive/refs/tags/v0.1.0.tar.gz',
    packages=find_packages(),
    install_requires=req,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.11',
        'Operating System :: OS Independent',
    ],
)
