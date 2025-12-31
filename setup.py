import setuptools
# 若Discription.md中有中文 須加上 encoding="utf-8"
with open("readme.md", "r",encoding="utf-8") as f:
    long_description = f.read()
    
setuptools.setup(
    name = "pydmsoft",
    version = "1.0.0",
    author = "Yi Ren.Song",
    author_email="8062825@gmail.com",
    description="A Simple python Wrapper for DM",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    install_requires=[
                    'comtypes',
                    'pywin32',
    ],
    packages=setuptools.find_packages(),     
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
    ],
    
    python_requires='>=3.10'
    )