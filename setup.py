import os

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))

requirements = []

requirements_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "requirements.txt"
)

with open(requirements_path) as req_file:
    for req_line in req_file:
        req_line = req_line.strip()
        if req_line.count("==") == 1:
            requirements.append(req_line)

setup(
    name="LibreView Lib",
    version="1.0.0",
    description="LibreView Lib",
    classifiers=[
      "Programming Language :: Python",
      "Programming Language :: Python :: 3"
    ],
    author="Dener Rodrigues",
    author_email="dl.rodrigues94@gmail.com",
    url="",
    keywords="",
    packages=find_packages(),
    setup_requires=["wheel"],
    include_package_data=True,
    zip_safe=False,
    install_requires=requirements,
    extras_require={},
    dependency_links=[]
)