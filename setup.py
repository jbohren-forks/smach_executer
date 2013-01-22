from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
  packages=['smach_executer'],
  scripts=['scripts/call_executer'],
  package_dir={'': 'src'}
)

setup(**d)
