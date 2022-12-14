"""Lightweight integration and denormalisation using events (signals)."""

from __future__ import annotations

from typing import Any

from blinker import ANY

from abilian.core.entities import Entity
from abilian.core.models.subjects import User
from abilian.core.signals import activity
from abilian.sbe.apps.documents.models import Document

from .models import Community


@activity.connect_via(ANY)
def update_community(
    sender: Any, verb: str, actor: User, object: Entity, target: Entity | None = None
):
    if isinstance(object, Community):
        object.touch()
        return

    if isinstance(target, Community):
        community = target
        community.touch()

        if isinstance(object, Document):
            if verb == "post":
                community.document_count += 1
            elif verb == "delete":
                community.document_count -= 1
