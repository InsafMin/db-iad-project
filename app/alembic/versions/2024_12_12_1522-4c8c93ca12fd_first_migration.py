"""first migration

Revision ID: 4c8c93ca12fd
Revises: 
Create Date: 2024-12-12 15:22:02.701413

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "4c8c93ca12fd"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "authors",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_authors")),
    )
    op.create_table(
        "readers",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("first_name", sa.String(), nullable=False),
        sa.Column("last_name", sa.String(), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_readers")),
        sa.UniqueConstraint("email", name=op.f("uq_readers_email")),
    )
    op.create_table(
        "books",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(), nullable=False),
        sa.Column("category", sa.String(), nullable=False),
        sa.Column(
            "published_year",
            sa.DateTime(),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column("author_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["author_id"],
            ["authors.id"],
            name=op.f("fk_books_author_id_authors"),
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_books")),
    )
    op.create_table(
        "copies",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("book_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["book_id"], ["books.id"], name=op.f("fk_copies_book_id_books")
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_copies")),
    )
    op.create_table(
        "borrowings",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("reader_id", sa.Integer(), nullable=False),
        sa.Column("copy_id", sa.Integer(), nullable=False),
        sa.Column(
            "borrow_date",
            sa.DateTime(),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column("return_date", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["copy_id"],
            ["copies.id"],
            name=op.f("fk_borrowings_copy_id_copies"),
        ),
        sa.ForeignKeyConstraint(
            ["reader_id"],
            ["readers.id"],
            name=op.f("fk_borrowings_reader_id_readers"),
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_borrowings")),
    )


def downgrade() -> None:
    op.drop_table("borrowings")
    op.drop_table("copies")
    op.drop_table("books")
    op.drop_table("readers")
    op.drop_table("authors")
