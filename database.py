import databases
import sqlalchemy
## DATABASE INITIALIZATION BEGIN{
DATABASE_URL = "sqlite:///data.db"  # could come from an env var
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

# POST TABLE
post_table = sqlalchemy.Table( ## CREATE TABLE FOR THE POST MODEL
    "posts",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String),
    sqlalchemy.Column("body", sqlalchemy.String),
    sqlalchemy.Column("user_id", sqlalchemy.ForeignKey("users.id"), nullable=False) # ADD RELATIONSHIP BETWEEN TABLES
)


comments_table = sqlalchemy.Table(
    "comments",
    metadata,
    sqlalchemy.Column("id",sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("body", sqlalchemy.String),
    sqlalchemy.Column("post_id", sqlalchemy.ForeignKey("posts.id"), nullable=False),
    sqlalchemy.Column("user_id", sqlalchemy.ForeignKey("users.id"), nullable=False),
)

# USER TABLE
user_table = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("username", sqlalchemy.String(30)),
    sqlalchemy.Column("password", sqlalchemy.String)
)


engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)


metadata.create_all(engine)

## END }