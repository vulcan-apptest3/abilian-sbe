Changelog for Abilian SBE
=========================


v0.5.21 (2021-08-02)
--------------------

- Cleanup.
- Drop support for Python < 3.8.


v0.5.7 (2020-01-02)
-------------------

- Fix for python 3.8.
- Py3k.


v0.5.6 (2019-10-08)
-------------------

Fix
~~~
- Bytes vs. str.

Other
~~~~~
- Refactor: cleanup.
- Py3k.


v0.5.5 (2019-08-07)
-------------------
- Type hints.
- Auto-generate authors.
- Cleanup.


v0.5.4 (2019-07-12)
-------------------
- F-strings.


0.5.3 (2019-06-28)
------------------
- Modernize (py36) / remove six.
- Runtime typechecker.
- Typing.
- Update dependency on Markdown.


v0.5.2 (2019-05-02)
-------------------
- Dont' use pylint.
- Modernize (py36)


v0.5.1 (2019-04-15)
-------------------
- Fix botched release.


0.5.0 (2019-04-15)
-------------------
- Drop Python 2 support and cleanup code accordingly.
- Various fixes.

0.4.25 (2019-01-07)
-------------------

- "Reply by email" fixes

0.4.22 (2019-01-02)
-------------------

- Use Poetry for packaging


0.4.19 (2018-12-26)
-------------------

- Cleanup small fixes related to updated dependencies.


0.4.13 (2018-08-02)
-------------------

- Fixes for Python 3.7
- Cleanup

0.4.10 (2018-06-11)
-------------------

- CSS fixes
- Deps updates

0.4.8 (2018-04-15)
------------------

- Fix for pip 10

0.4.5 (2018-02-22)
------------------

- JS cleanup

0.4.2 (2018-01-04)
------------------

- Fix errors on document delete
- Cleanup code

0.4.1 (2018-01-03)
------------------

- Previous release was broken.

0.4.0 (2018-01-03)
------------------

- Completely revamped document management UI


0.3.17 (2017-10-02)
-------------------

- Remove unwanted button
- Cleanup and prepare for the future

0.3.13 (2017-08-02)
-------------------

- Clean up and work towards migration to Python 3.

0.3.12 (2017-08-01)
-------------------

- Clean up and work towards migration to Python 3.

0.3.10 (2017-07-03)
-------------------

- Fix HTML bug on the forum that prevents work under Firefox.

0.3.9 (2017-06-26)
------------------

- Fix regression on community members.

0.3.8 (2017-06-23)
------------------

- Wizard to import users in communities.

0.3.7 (2017-06-22)
------------------

- Forum UI tweaks.

0.2.6 (2016-05-06)
------------------

- Test fixes.

0.2.5 (2016-04-25)
------------------

- Fix unicode encoding issue.

0.2.2 (2016-03-03)
------------------

- Get rid of guess-language-spirit. Use langid instead.

0.2.1 (2016-02-15)
------------------

- Documents: can upload a new version if nobody has locked the document.
- Fix daily notifications (for wiki pages).

0.2.0 (2016-02-12)
------------------

Time for a minor release.

0.1.10 (2016-02-05)
-------------------

- forum reply by mail: changed reply address so that it's local part never
  exceeds 64 characters length

0.1.9 (2016-01-29)
------------------

- Fix error when sending the daily digest.

0.1.8 (2016-01-29)
------------------

- Fix packaging issue (missing .mo files).

0.1.7 (2016-01-29)
------------------

- Communities can be linked to a group. Members are 2-way synced.


0.1.5 (2015-11-20)
------------------

- Members: export listing in xslx format
- Documents are reindexed on permissions or membership change
- Conversations can be closed by admin for edit/new comments/deletion
- Fix global activity stream for non-admin users


0.1.4 (2015-08-07)
------------------

- Add "wall of attachments" in communities
- Use pdfjs to preview documents on browsers
- Fix 'refresh preview' action on documents
- UX/UI improvements


0.1.3 (2015-07-29)
------------------

- Various CSS and HTML improvements / fixes.


0.1.2 (2015-07-15)
------------------

Improvements
~~~~~~~~~~~~

- Design / CSS

Fixes
~~~~~

- Fix sqlalchemy connection issues with Celery tasks

Refactoring
~~~~~~~~~~~

- JS: Use requirejs


0.1.1 (2015-05-27)
------------------

Improvements
~~~~~~~~~~~~

*  community views: support graceful csrf failure
*  added attachment to forum post by email
*  added attachments views in forum
*  forum post: show 'send by mail' only if enabled for community or current user
*  i18n on roles

Fixes
~~~~~

* fix css rule for 'recent users' box
*  communities settings forms:  fix imagefield arguments
*  NavAction Communities is now only showed when authenticated
*  added regex clean forum posts from email

Refactoring
~~~~~~~~~~~

*  folder security: use Permission/Role objects
*  * views/social.py: remove before_request
*  forum views: use CBV
*  forum: form factorisation
*  @login_required on community index and social.wall, has_access() stops anonymous users
*  pep8 cleanup
*  tests/functional  port is now dynamic to avoid runtime errors
*  replaced csrf_field -> csrf.field() in thread.html to have proper csrf and allow action to go on (#16)
*  unescaped activity entry body_html
*  fix test: better mock of celery task
*  abilian-core removed extensions.celery; use periodic_task from abilian.core.celery
*  forum: in-mail tasks: set app default config values; conditionnaly register check_maildir
*  celery: use 'shared_task' decorator

0.1 (2015-03-31)
----------------

Initial release
