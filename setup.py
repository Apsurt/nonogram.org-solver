from setuptools import setup, find_packages
# noinspection PyPep8Naming
from setuptools.command.test import test as TestCommand
from setuptools import Command
from subprocess import call
from codecs import open
import os
import sys

if sys.version_info.major < 3:
    sys.exit('Python 2 is not supported')


# noinspection PyCallByClass,PyAttributeOutsideInit
class PyTest(TestCommand):
    user_options = [('pytest-args', 'a', 'Arguments to pass into py.test')]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


class Publish(Command):
    description = 'Automate all the boring stuff when releasing the package'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        os.system('python setup.py register')
        os.system('python setup.py sdist upload')
        os.system('python setup.py bdist_wheel upload')
        os.system('python setup.py bdist upload')
        print('All done!')
        sys.exit()


test_requirements = ['pytest>=3.0.3']

requirements = ['PyYAML>=3.11', 'jsonpickle>=0.9.3']

if os.path.isfile('requirements.txt'):
    with open('requirements.txt', encoding='utf-8') as f:
        requirements.extend(f.readlines())

if sys.version_info.minor < 5:
    requirements.append('typing>=3.5.2.2')

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(name='pyNonogram',
      version='0.1.0',
      description='',
      long_description=long_description,
      url='https://github.com/Apsurt/pyNonogram',
      author='Tymon Becella',
      author_email='tymon.becella@gmail.com',
      license='MIT',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Games/Entertainment',
          'Topic :: Utilities',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3 :: Only',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: Implementation :: PyPy'
      ],
      keywords='nonogram nonograms griddlers picross pic-a-pix paintbynumbers puzzle puzzles',
      packages=find_packages(exclude=['tests', 'docs', 'examples']),
      install_requires=requirements,
      cmdclass={'test': PyTest, 'publish': Publish},
      tests_require=test_requirements,
      include_package_data=True
      )