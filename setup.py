from setuptools import setup, find_packages
setup(
    name='kaushal_tools',
    version='0.1',
    packages=find_packages(),
    description='These package was created to simplify some of components',
    author="Kaushal Bhatol",
    install_requires=[
        # List your package dependencies here
        'qrcode',
        'opencv-python',
        'cryptography'
    ],
)
