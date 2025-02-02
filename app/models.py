# -*- coding: utf-8 -*-
from datetime import datetime, timezone
from typing import Optional

import sqlalchemy as sa
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
    __tablename__ = "notifications"

    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    event_id: so.Mapped[str] = so.mapped_column(index=True)
    namespace: so.Mapped[Optional[str]]
    name: so.Mapped[Optional[str]] = so.mapped_column(index=True)
    descr: so.Mapped[Optional[str]]
    event_type: so.Mapped[Optional[str]] = so.mapped_column(index=True)
    category: so.Mapped[Optional[str]] = so.mapped_column(index=True)
    domain: so.Mapped[Optional[str]] = so.mapped_column(index=True)
    subdomain: so.Mapped[Optional[str]]
    severity: so.Mapped[int] = so.mapped_column(
        sa.CheckConstraint("severity BETWEEN 1 AND 5", name="severity"), index=True
    )
    source: so.Mapped[Optional[str]] = so.mapped_column(index=True)
    _timestamp: so.Mapped[Optional[str]]
    details_type: so.Mapped[Optional[str]]
    priority: so.Mapped[Optional[str]] = so.mapped_column(index=True)
    device: so.Mapped[Optional[str]] = so.mapped_column(index=True)
    issue: so.Mapped[Optional[str]]
    issue_name: so.Mapped[Optional[str]]
    issue_category: so.Mapped[Optional[str]] = so.mapped_column(index=True)
    status: so.Mapped[Optional[str]] = so.mapped_column(index=True)
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

    @hybrid_property
    def is_critical(self) -> bool:
        return self.severity == 1

    @hybrid_property
    def is_resolved(self) -> bool:
        return self.status and self.status.lower() == "resolved"

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
