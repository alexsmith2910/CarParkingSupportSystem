from uuid import uuid4


class Ticket:
    _loaded = {}
    ticket_id = None

    def __new__(cls, ticket_id, _loaded_from_db=False):
        if isinstance(ticket_id, str) and _loaded_from_db is False:
            return None

        if (cls_ticket := cls._loaded.get(ticket_id)) is not None:
            print(f"Returning existing client from cache ({cls_ticket})")
            return cls_ticket

        cls_ticket = super().__new__(cls)
        cls._loaded[ticket_id] = cls_ticket
        return cls_ticket

    def __init__(self, ticket_id, _loaded_from_db=False):
        self.ticket_id = str(ticket_id)

    @staticmethod
    def generate_new_ticket():
        return Ticket(uuid4())

    @staticmethod
    def load_from_database(ticket_id):
        return Ticket(ticket_id, _loaded_from_db=True)
