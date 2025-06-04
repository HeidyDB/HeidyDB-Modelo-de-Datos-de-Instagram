from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, Integer, enum
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)

class Post(db.Model):
    id: Mapped[int]= mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer)


class Follower(db.Model):
    user_from_id: Mapped[int]= mapped_column(primary_key=True)
    user_to_id: Mapped[int]= mapped_column(primary_key=True)

class Media(db.Model):
    id: Mapped[int]= mapped_column(Integer , primary_key=True)
    url: Mapped[str] = mapped_column(String)
    type: Mapped[enum] = mapped_column(Integer)
    




    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
