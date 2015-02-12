from setuptools import setup


version = '0.5.8'

setup(
    name='strapmin',
    version=version,
    packages=['strapmin'],
    include_package_data=True,
    author='Tom Carrick',
    author_email='knyght@knyg.ht',
    license='BSD 2 Clause',
    long_description='A bootstrappy django admin reskin',
    description='A bootstrappy django admin reskin',
    install_requires=['django >= 1.5'],
    requires=['django (>= 1.5)'],
)
