"""role update

Revision ID: f37951e526a1
Revises: cc4b1d65ff77
Create Date: 2024-03-12 12:51:55.712874

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f37951e526a1'
down_revision: Union[str, None] = 'cc4b1d65ff77'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
