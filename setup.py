from setuptools import setup, find_packages

with open("requirements.txt") as f:
    install_requires = [
        line for line in f.read().strip().split("\n")
        if line and not line.startswith("#")
    ]

setup(
    name="civic_erp",
    version="0.0.1",
    description="ERP for Government Bodies and Non-Profit Organizations",
    author="bizaxl",
    author_email="admin@bizaxl.com",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires,
)
