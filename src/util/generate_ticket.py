from uuid import uuid4


class Ticket:
    _loaded = {}
    ticket_id = None

    def __new__(cls, ticket):
        if (cls_ticket := cls._loaded.get(ticket)) is not None:
            print(f"Returning existing client from cache ({cls_ticket})")
            return cls_ticket

        cls_ticket = super().__new__(cls)
        cls._loaded[ticket] = cls_ticket
        return cls_ticket

    def __init__(self, ticket):
        self.ticket_id = self.generate_ticket_id()

    @staticmethod
    def generate_ticket_id():
        return uuid4()
