from datetime import datetime, timezone
from typing import Optional

import sqlalchemy.orm as so

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
    timestamp: so.Mapped[Optional[int]]
    details_type: so.Mapped[Optional[str]]
    priority: so.Mapped[Optional[str]]
    device: so.Mapped[Optional[str]]
    issue: so.Mapped[Optional[str]]
    issue_name: so.Mapped[Optional[str]]
    issue_category: so.Mapped[Optional[str]]
    status: so.Mapped[Optional[str]]
    link: so.Mapped[Optional[str]]

    def __repr__(self):
        return f"<Notification {self.id!r}, {self.priority!r}, {self.severity!r}, {self.name!r}>"
