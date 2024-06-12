class Band:
    def __init__(self, name, hometown):
        if not isinstance(name, str) or len(name) == 0:
            raise Exception("Band name must be a non-empty string.")
        self._name = name

        if not isinstance(hometown, str) or len(hometown) == 0:
            raise Exception("Band hometown must be a non-empty string.")
        self._hometown = hometown
        
        self._concerts = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise Exception("Band name must be a non-empty string.")
        self._name = value

    @property
    def hometown(self):
        return self._hometown

    @property
    def concerts(self):
        return self._concerts if self._concerts else None

    @property
    def venues(self):
        unique_venues = list(set(concert.venue for concert in self._concerts))
        return unique_venues if unique_venues else None

    def play_in_venue(self, venue, date):
        from concert import Concert
        concert = Concert(date, self, venue)
        self._concerts.append(concert)
        return concert

    def all_introductions(self):
        if not self._concerts:
            return None
        return [concert.introduction() for concert in self._concerts]