# -*- coding: utf-8 -*-
from datetime import datetime, timezone
from typing import Optional

import sqlalchemy.orm as so
from sqlalchemy.ext.hybrid import hybrid_property

from app import db


class TimestampMixin:
    created: so.Mapped[datetime] = so.mapped_column(
        default=lambda: datetime.now(timezone.utc)
    )
    updated: so.Mapped[datetime] = so.mapped_column(
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )


class Notification(TimestampMixin, db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    event_id: so.Mapped[Optional[str]]
    namespace: so.Mapped[Optional[str]]
    name: so.Mapped[Optional[str]]
    descr: so.Mapped[Optional[str]]
    event_type: so.Mapped[Optional[str]]
    category: so.Mapped[Optional[str]]
    domain: so.Mapped[Optional[str]]
    subdomain: so.Mapped[Optional[str]]
    severity: so.Mapped[Optional[int]]
    source: so.Mapped[Optional[str]]
    _timestamp: so.Mapped[Optional[int]]
    details_type: so.Mapped[Optional[str]]
    priority: so.Mapped[Optional[str]]
    device: so.Mapped[Optional[str]]
    issue: so.Mapped[Optional[str]]
    issue_name: so.Mapped[Optional[str]]
    issue_category: so.Mapped[Optional[str]]
    status: so.Mapped[Optional[str]]
    link: so.Mapped[Optional[str]]

    @hybrid_property
    def timestamp(self) -> int | float:
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value):
        self._timestamp = datetime.fromtimestamp(value / 1000, timezone.utc)

    @timestamp.expression
    def timestamp(cls):
        return cls._timestamp

    @property
    def serialize(self) -> dict[str, str | int | float]:
        return {
            "code": (
                "<span class='status-dot status-green'></span>"
                if self.status == "resolved"
                else "<span class='status-dot status-red'></span>"
            ),
            "eventId": self.event_id,
            "namespace": self.namespace,
            "name": self.name,
            "descr": self.descr,
            "eventType": self.event_type,
            "category": self.category,
            "domain": self.domain,
            "subDomain": self.subdomain,
            "severity": self.severity,
            "source": self.source,
            "timestamp": self.timestamp,
            "detailsType": self.details_type,
            "priority": self.priority,
            "device": self.device,
            "issue": self.issue,
            "issueName": self.issue_name,
            "issueCategory": self.issue_category,
            "status": self.status,
            "link": self.link,
        }

    def __repr__(self):
        return f"<Notification {self.id!r}, {self.priority!r}, {self.severity!r}, {self.name!r}, {self.status!r}>"
