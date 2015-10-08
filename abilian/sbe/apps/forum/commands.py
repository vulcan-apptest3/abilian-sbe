# coding=utf-8
"""

"""
from __future__ import absolute_import

import logging
import fileinput
from email.parser import FeedParser

from flask_script import Manager

from .tasks import process_email, check_maildir

logger = logging.getLogger(__name__)


manager = Manager(description='SBE forum commands',
                  help='SBE forum commands')


@manager.command
def inject_email():
  """
  Reads one email from stdin,
  parse it,
  forward it in a celery task to be persisted.
  """
  parser = FeedParser()
  message = None
  try:
    # iterate over stdin
    for line in fileinput.input('-'):
      parser.feed(line)
  except:
    logger.error('Error during email parsing', exc_info=True)
  finally:
    # close the parser to generate a email.message
    message = parser.close()
    fileinput.close()

  if message:
    # make sure no email.errors are present
    if len(message.defects) == 0:
      process_email.delay(message)
    else:
      logger.error('email has defects')
  else:
    logger.error('no email was parsed from stdin')


@manager.command
def check_email():
  """
  Reads one email from current user Maildir,
  parse it,
  forward it in a celery task to be persisted.
  """

  check_maildir.delay()
