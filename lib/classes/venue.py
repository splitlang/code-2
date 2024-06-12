class Venue:
    def __init__(self, name, city):
        if not isinstance(name, str) or len(name) == 0:
            raise Exception("Venue name must be a non-empty string.")
        self._name = name

        if not isinstance(city, str) or len(city) == 0:
            raise Exception("Venue city must be a non-empty string.")
        self._city = city

        self._concerts = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise Exception("Venue name must be a non-empty string.")
        self._name = value

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise Exception("Venue city must be a non-empty string.")
        self._city = value

    def concerts(self):
        return self._concerts if self._concerts else None

    def bands(self):
        unique_bands = list(set(concert.band for concert in self._concerts))
        return unique_bands if unique_bands else None

    def concert_on(self, date):
        for concert in self._concerts:
            if concert.date == date:
                return concert
        return None