import os.path
from setuptools import setup

version = '4.1.dev0'

install_requires = []

here = os.path.abspath(os.path.dirname(__file__))
try:
    README = open(os.path.join(here, 'README.rst')).read()
    CHANGES = open(os.path.join(here, 'CHANGES.rst')).read()
except IOError:
    README = CHANGES = ''

setup(
    name='python-gettext',
    version=version,
    description="Python Gettext po to mo file compiler.",
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Internationalization',
        'Topic :: Software Development :: Localization',
    ],
    keywords='Python Gettext Msgctxt',
    author='Hanno Schlichting',
    author_email='hanno@hannosch.eu',
    url='https://github.com/hannosch/python-gettext',
    license='BSD',
    packages=['pythongettext', 'pythongettext.tests'],
    install_requires=install_requires,
    include_package_data=True,
    zip_safe=False,
    test_suite="pythongettext.tests",
)
