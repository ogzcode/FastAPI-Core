"""role update

Revision ID: 0f2e17e94d6b
Revises: f37951e526a1
Create Date: 2024-03-12 12:51:58.025666

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0f2e17e94d6b'
down_revision: Union[str, None] = 'f37951e526a1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
