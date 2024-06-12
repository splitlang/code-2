class Band:
    def __init__(self, name, hometown):
        if not isinstance(name, str) or len(name) == 0:
            raise AssertionError("Band name must be a non-empty string.")
        self._name = name

        if not isinstance(hometown, str) or len(hometown) == 0:
            raise AssertionError("Band hometown must be a non-empty string.")
        self._hometown = hometown
        
        self._concerts = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise AssertionError("Band name must be a non-empty string.")
        self._name = value

    @property
    def hometown(self):
        return self._hometown

    def _set_hometown(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise AssertionError("Band hometown must be a non-empty string.")
        self._hometown = value

    def concerts(self):
        return self._concerts

    def venues(self):
        return list(set(concert.venue for concert in self._concerts))

    def play_in_venue(self, venue, date):
        from concert import Concert
        if not isinstance(venue, Venue):
            raise AssertionError("Venue must be a Venue instance.")
        if not isinstance(date, str) or len(date) == 0:
            raise AssertionError("Concert date must be a non-empty string.")
        concert = Concert(date, self, venue)
        return concert

    def all_introductions(self):
        return [concert.introduction() for concert in self._concerts] if self._concerts else None

class Concert:
    def __init__(self, date, band, venue):
        if not isinstance(date, str) or len(date) == 0:
            raise AssertionError("Concert date must be a non-empty string.")
        self._date = date

        if not isinstance(band, Band):
            raise AssertionError("Concert band must be a Band instance.")
        self._band = band

        if not isinstance(venue, Venue):
            raise AssertionError("Concert venue must be a Venue instance.")
        self._venue = venue

        band._concerts.append(self)
        venue._concerts.append(self)

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise AssertionError("Concert date must be a non-empty string.")
        self._date = value

    @property
    def band(self):
        return self._band

    @band.setter
    def band(self, value):
        if not isinstance(value, Band):
            raise AssertionError("Concert band must be a Band instance.")
        self._band = value

    @property
    def venue(self):
        return self._venue

    @venue.setter
    def venue(self, value):
        if not isinstance(value, Venue):
            raise AssertionError("Concert venue must be a Venue instance.")
        self._venue = value

    def hometown_show(self):
        return self._band.hometown == self._venue.city

    def introduction(self):
        return f"Hello {self._venue.city}!!!!! We are {self._band.name} and we're from {self._band.hometown}"

class Venue:
    def __init__(self, name, city):
        if not isinstance(name, str) or len(name) == 0:
            raise AssertionError("Venue name must be a non-empty string.")
        self._name = name

        if not isinstance(city, str) or len(city) == 0:
            raise AssertionError("Venue city must be a non-empty string.")
        self._city = city

        self._concerts = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise AssertionError("Venue name must be a non-empty string.")
        self._name = value

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise AssertionError("Venue city must be a non-empty string.")
        self._city = value

    def concerts(self):
        return self._concerts

    def bands(self):
        return list(set(concert.band for concert in self._concerts))

    def concert_on(self, date):
        for concert in self._concerts:
            if concert.date == date:
                return concert
        return None