from sqlalchemy import BigInteger, Integer
from app.extensions import db
from flask_login import UserMixin
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional
import json

# SQLite treats all ints as the same, so we want to make sure other variants can use a big integer
ID_TYPE = BigInteger().with_variant(Integer, "sqlite")


class User(db.Model, UserMixin):
    '''
    Represents a user in the system.

    Attributes:
        id (int): The unique identifier for the user.
        username (Optional[str]): The username of the user.
        overlay (Overlay): The overlay associated with the user.

    Methods:
        __repr__() -> str:
            Returns a string representation of the user.
        
        to_dict() -> dict:
            Converts the user instance to a dictionary.
    '''
    id: Mapped[int] = mapped_column(ID_TYPE, primary_key=True)
    username: Mapped[Optional[str]]
    overlay: Mapped["Overlay"] = relationship(back_populates="user")

    def __repr__(self) -> str:
        return f"<User {self.id} - {self.overlay}>"

    def to_dict(self) -> dict:
        '''
        Converts the model instance to a dictionary representation.

        Returns:
            dict: A dictionary containing the model's id, username, and overlay.
                  The overlay is also converted to a dictionary if it exists, otherwise None.
        '''
        return {
            "id": self.id,
            "username": self.username,
            "overlay": self.overlay.to_dict() if self.overlay else None
        }

class Overlay(db.Model):
    '''
    Overlay Model

    Attributes:
        id (str): The primary key of the overlay.
        user_id (int): The foreign key referencing the user.
        user (User): The relationship to the User model.
        player1_commander1 (Optional[str]): The first commander for player 1.
        player1_commander1_ci (Optional[str]): The commander information for player 1's first commander.
        player1_commander2 (Optional[str]): The second commander for player 1.
        player1_commander2_ci (Optional[str]): The commander information for player 1's second commander.
        player2_commander1 (Optional[str]): The first commander for player 2.
        player2_commander1_ci (Optional[str]): The commander information for player 2's first commander.
        player2_commander2 (Optional[str]): The second commander for player 2.
        player2_commander2_ci (Optional[str]): The commander information for player 2's second commander.
        player3_commander1 (Optional[str]): The first commander for player 3.
        player3_commander1_ci (Optional[str]): The commander information for player 3's first commander.
        player3_commander2 (Optional[str]): The second commander for player 3.
        player3_commander2_ci (Optional[str]): The commander information for player 3's second commander.
        player4_commander1 (Optional[str]): The first commander for player 4.
        player4_commander1_ci (Optional[str]): The commander information for player 4's first commander.
        player4_commander2 (Optional[str]): The second commander for player 4.
        player4_commander2_ci (Optional[str]): The commander information for player 4's second commander.

    Methods:
        __repr__() -> str:
            Returns a string representation of the Overlay instance.
        to_dict() -> dict:
        update(data: dict) -> None:
    '''
    id: Mapped[str] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ID_TYPE, db.ForeignKey('user.id'), nullable=False)
    user: Mapped["User"] = relationship(back_populates="overlay")
    player1_commander1: Mapped[Optional[str]]
    player1_commander1_ci: Mapped[Optional[str]]
    player1_commander2: Mapped[Optional[str]]
    player1_commander2_ci: Mapped[Optional[str]]
    player2_commander1: Mapped[Optional[str]]
    player2_commander1_ci: Mapped[Optional[str]]
    player2_commander2: Mapped[Optional[str]]
    player2_commander2_ci: Mapped[Optional[str]]
    player3_commander1: Mapped[Optional[str]]
    player3_commander1_ci: Mapped[Optional[str]]
    player3_commander2: Mapped[Optional[str]]
    player3_commander2_ci: Mapped[Optional[str]]
    player4_commander1: Mapped[Optional[str]]
    player4_commander1_ci: Mapped[Optional[str]]
    player4_commander2: Mapped[Optional[str]]
    player4_commander2_ci: Mapped[Optional[str]]

    def __repr__(self) -> str:
        return f"<Overlay {self.id}>"

    def to_dict(self) -> dict:
        '''
        Converts the instance attributes to a dictionary.

        Returns:
            dict: A dictionary representation of the instance with the following keys:
                - id: The ID of the instance.
                - user_id: The user ID associated with the instance.
                - player1_commander1: The first commander for player 1.
                - player1_commander1_ci: The commander information for player 1's first commander.
                - player1_commander2: The second commander for player 1.
                - player1_commander2_ci: The commander information for player 1's second commander.
                - player2_commander1: The first commander for player 2.
                - player2_commander1_ci: The commander information for player 2's first commander.
                - player2_commander2: The second commander for player 2.
                - player2_commander2_ci: The commander information for player 2's second commander.
                - player3_commander1: The first commander for player 3.
                - player3_commander1_ci: The commander information for player 3's first commander.
                - player3_commander2: The second commander for player 3.
                - player3_commander2_ci: The commander information for player 3's second commander.
                - player4_commander1: The first commander for player 4.
                - player4_commander1_ci: The commander information for player 4's first commander.
                - player4_commander2: The second commander for player 4.
                - player4_commander2_ci: The commander information for player 4's second commander.
        '''
        return {
            "id": self.id,
            "user_id": self.user_id,
            "player1_commander1": self.player1_commander1,
            "player1_commander1_ci": self.player1_commander1_ci,
            "player1_commander2": self.player1_commander2,
            "player1_commander2_ci": self.player1_commander2_ci,
            "player2_commander1": self.player2_commander1,
            "player2_commander1_ci": self.player2_commander1_ci,
            "player2_commander2": self.player2_commander2,
            "player2_commander2_ci": self.player2_commander2_ci,
            "player3_commander1": self.player3_commander1,
            "player3_commander1_ci": self.player3_commander1_ci,
            "player3_commander2": self.player3_commander2,
            "player3_commander2_ci": self.player3_commander2_ci,
            "player4_commander1": self.player4_commander1,
            "player4_commander1_ci": self.player4_commander1_ci,
            "player4_commander2": self.player4_commander2,
            "player4_commander2_ci": self.player4_commander2_ci,
        }

    def update(self, data: dict) -> None:
        '''
        Updates the attributes of the instance with the provided data and commits the changes to the database.

        Args:
            data (dict): A dictionary containing key-value pairs where the key is the attribute name and the value is the new value to be set.

        Returns:
            None
        '''
        for key, value in data.items():
            setattr(self, key, value)
        db.session.commit()
