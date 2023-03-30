Changelog
=========

5.0 (unreleased)
----------------

- Add support for Python 3.11.

- Drop support for Python 2.7, 3.5, 3.6.


4.1 (2022-08-26)
----------------

- Add support for Python 3.8, 3.9, 3.10. [icemac]

- Drop support for Python 3.4. [icemac]

- Drop support for running the tests using ``python setup.py test``. [icemac]


4.0 (2018-11-27)
----------------

- Add support for Python 3.6 and 3.7.
  [sallner]

- Drop support for Python 2.6.
  [sallner]


3.0 - 2016-01-04
----------------

- Use `u''` strings again for easier cross Python 2/3 code.
  [hannosch]

- #5: Fix plural form support under Python 3.x.
  [hannosch]

- Break dependency on ``unittest2`` for Python 2.7.
  [icemac]

2.1 - 2013-02-10
----------------

- Prefer `ast.literal_eval` over `eval` under Python 2, instead of just under
  Python 3. We only support Python 2.6+ where the function is available.
  [hannosch]

- Tested successfully under Python 3.3.
  [hannosch]

2.0 - 2011-12-22
----------------

- Tested successfully under PyPy 1.7.
  [hannosch]

- Handle non-latin-1 characters in the header correctly.
  [hannosch]

- Python 2 and 3 compatibility in the same codebase.
  [hannosch]

1.2 - 2011-11-01
----------------

- Make sure empty `po` files don't break.
  [Alexandru Plugaru]

- Add support for messages with plural forms.
  [Andrei Polushin]

1.1.1 - 2011-03-21
------------------

- Simplify test folder discovery.
  [hannosch]

1.1 - 2011-03-20
----------------

- Handle Unicode Byte Order Mark at the beginning of files. This closes
  http://dev.plone.org/plone/ticket/10813.
  [hannosch, kleist]

- Fixed potential UnicodeError in exception handling. This closes
  http://dev.plone.org/plone/ticket/11058.
  [hannosch, vincentfretin]

1.0 - 2009-05-23
----------------

- Updated package description and metadata, relicense from GPL to BSD. Note
  about Babel which supersedes this package in all possible ways.
  [hannosch]

0.6 - 2007-11-02
----------------

- Fixed header parsing.
  [hannosch]

0.5 - 2007-11-01
----------------

- Optimized file parsing by using more elif clauses and avoiding an insane
  number of startswith and isinstance calls.
  [hannosch]

0.4 - 2007-10-13
----------------

- Added header_only argument to the read method, that allows to only parse
  the header of a file without reading and parsing all the messages.
  [hannosch]

0.3 - 2007-08-25
----------------

- Added an explicit read method, which only parses the po file and stores
  it in the messages dict, but does not compile it.
  [hannosch]

0.2 - 2007-08-23
----------------

- Bumped version number to accommodate the number in the egg info.
  [hannosch]

0.1 - 2007-06-19
----------------

- Initial implementation of a Msgfmt class which supports the generation of
  Gettext mo files including support for the new msgctxt keyword.
  [hannosch]
