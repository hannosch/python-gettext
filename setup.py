from setuptools import setup, find_packages

version = '0.6'

setup(name='python-gettext',
      version=version,
      description="Python Gettext implementation.",
      long_description="""\
This implementation of Gettext for Python includes a Msgfmt class which can be
used to generate compiled mo files from Gettext po files and includes support
for the newer msgctxt keyword.""",
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Internationalization',
        'Topic :: Software Development :: Localization',
      ],
      keywords='Python Gettext Msgctxt',
      author='Hanno Schlichting',
      author_email='hanno@hannosch.info',
      url='http://svn.plone.org/svn/collective/python-gettext/trunk',
      license='GPL',
      packages=find_packages(exclude=['ez_setup', 'tests']),
      include_package_data=True,
      zip_safe=False,
      )
