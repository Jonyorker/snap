
from setuptools import setup, find_packages

setup(
    name="Incuvers IOT App",
    version="1.0.0",
    long_description=__doc__,
    # packages=["app"],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=["Flask"],
)
