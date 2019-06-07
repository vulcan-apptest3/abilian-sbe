# coding=utf-8
""""""
from datetime import datetime, timedelta

import dateutil.parser
from abilian.core.util import utcnow
from flask import current_app
from flask_login import current_user

DEFAULT_LIFETIME = 3600


class Lock:
    """Represent a lock on a document."""

    def __init__(self, user_id, user, date, *args, **kwargs):
        self.user_id = user_id
        self.user = user
        if not isinstance(date, datetime):
            try:
                date = dateutil.parser.parse(date)
            except Exception as e:
                raise ValueError(f"Error parsing date: {date!r}") from e

        self.date = date

    @staticmethod
    def new():
        return Lock(current_user.id, str(current_user), utcnow())

    def as_dict(self):
        """Return a dict suitable for serialization to JSON."""
        return {
            "user_id": self.user_id,
            "user": self.user,
            "date": self.date.isoformat(),
        }

    @staticmethod
    def from_dict(d):
        """Deserialize from a `dict` created by :meth:`as_dict`."""
        return Lock(**d)

    @property
    def lifetime(self) -> int:
        return current_app.config.get("SBE_LOCK_LIFETIME", DEFAULT_LIFETIME)

    @property
    def expired(self) -> bool:
        return (utcnow() - self.date) > timedelta(seconds=self.lifetime)

    def is_owner(self, user=None):
        if user is None:
            user = current_user

        return self.user_id == user.id
