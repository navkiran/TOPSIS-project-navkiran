import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="topsis_navkiran", 
    version="0.0.4",
    author="Navkiran Singh",
    author_email="nsingh2_be17@thapar.edu",
    description="TOPSIS implementation in python for multi-criteria decision making",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/navkiran/topsis_project_navkiran",
    packages=setuptools.find_packages(),
    keywords = ['command-line', 'topsis-python', 'TOPSIS'],  
    install_requires=[            
          'numpy',
          'pandas',
      ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
