import attr


@attr.s(slots=True, order=True)
class CardAccess:
    card_id: str = attr.ib(converter=str)

    def to_readable(self):
        return {"card_id": self.card_id}

