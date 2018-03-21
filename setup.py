from setuptools import setup
from puzh import __version__


with open('README.rst') as file:
    readme = file.read()

setup(name='puzh',
      packages=['puzh'],
      version=__version__,
      author='lmittmann',
      description='Easily send messages to telegram',
      long_description=readme,
      keywords=['puzh', 'push', 'telegram', 'bot', 'notification'],
      url='https://github.com/puzh/puzh.py',
      license='MIT',
      python_requires='>=3',
      install_requires=['requests>=2.4.2'])
