import attr
import datetime

from src.models.card import CardAccess


@attr.s(slots=True, order=True)
class User:
    ticket_id: str = attr.ib(converter=str)
    time_of_entry: datetime.datetime = attr.ib(validator=attr.validators.instance_of(datetime.datetime))
    has_card: bool = attr.ib(validator=attr.validators.instance_of(bool))
    time_of_exit: datetime.datetime = attr.ib(default=None)
    card: dict = attr.ib(default={})

    def get_duration(self):
        if self.time_of_exit is None:
            return None
        return self.time_of_exit - self.time_of_entry

    @staticmethod
    def load_from_database(data):
        try:
            return User(data["ticketID"],
                        data["time_of_entry"],
                        data["has_card"],
                        data["time_of_exit"],
                        data["card"])
        except Exception as e:
            return None
