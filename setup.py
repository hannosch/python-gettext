from setuptools import setup

version = '1.1'


setup(name='python-gettext',
      version=version,
      description="Python Gettext po to mo file compiler.",
      long_description=open("README.rst").read() +  "\n" +
                       open("CHANGES.txt").read(),
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
      author_email='hanno@hannosch.eu',
      url='http://pypi.python.org/pypi/python-gettext',
      license='BSD',
      packages=['pythongettext', 'pythongettext.tests'],
      install_requires=['unittest2'],
      )
