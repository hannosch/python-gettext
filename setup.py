from setuptools import setup, find_packages

version = '1.0'

setup(name='python-gettext',
      version=version,
      description="Python Gettext implementation.",
      long_description="""\
This implementation of Gettext for Python includes a Msgfmt class which can be
used to generate compiled mo files from Gettext po files and includes support
for the newer msgctxt keyword. The idea for this project had been rather
ambitious, but never lived up to what is was supposed to do. Look at Babel
(http://pypi.python.org/pypi/Babel) for a package more worthy of this
packages' name.
""",
      classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Internationalization',
        'Topic :: Software Development :: Localization',
      ],
      keywords='Python Gettext Msgctxt',
      author='Hanno Schlichting',
      author_email='hannosch@hannosch.eu',
      url='http://pypi.python.org/pypi/python-gettext',
      license='BSD',
      packages=find_packages(exclude=['ez_setup', 'tests']),
      include_package_data=True,
      zip_safe=False,
      )
