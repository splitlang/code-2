class Concert:
    def __init__(self, date, band, venue):
        from band import Band
        from venue import Venue

        if not isinstance(date, str) or len(date) == 0:
            raise Exception("Concert date must be a non-empty string.")
        self._date = date

        if not isinstance(band, Band):
            raise Exception("Concert band must be a Band instance.")
        self._band = band

        if not isinstance(venue, Venue):
            raise Exception("Concert venue must be a Venue instance.")
        self._venue = venue

        venue._concerts.append(self)

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise Exception("Concert date must be a non-empty string.")
        self._date = value

    @property
    def band(self):
        return self._band

    @band.setter
    def band(self, value):
        from band import Band
        if not isinstance(value, Band):
            raise Exception("Concert band must be a Band instance.")
        self._band = value

    @property
    def venue(self):
        return self._venue

    @venue.setter
    def venue(self, value):
        from venue import Venue
        if not isinstance(value, Venue):
            raise Exception("Concert venue must be a Venue instance.")
        self._venue = value

    def hometown_show(self):
        return self._band.hometown == self._venue.city

    def introduction(self):
        return f"Hello {self._venue.city}!!!!! We are {self._band.name} and we're from {self._band.hometown}"
