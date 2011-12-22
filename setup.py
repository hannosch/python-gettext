from setuptools import setup

version = '1.3dev'


setup(name='python-gettext',
      version=version,
      description="Python Gettext po to mo file compiler.",
      long_description=open("README.rst").read() +  "\n" +
                       open("CHANGES.txt").read(),
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
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
      include_package_data = True,
      zip_safe = False,
      )
