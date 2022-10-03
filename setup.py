from setuptools import setup, find_packages

setup(
    name='redpandas',
    version='0.0.0',
    description='Python libaray which helps manage notion with dataframe',
    url='',
    author='Kyoungwhan Mheen',
    author_email='kwmheen@gmail.com',
    packages=find_packages(),
    zip_safe=False,
    install_requires=['SQLAlchemy==1.4.*']
)
