class DVD:
    def __init__(self, name: str, id: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, id: int, name: str, date: str, age_restriction: int):
        month = {'01': 'Janauary',
                 '02': 'February',
                 '03': 'March',
                 '04': 'April',
                 '05': 'May',
                 '06': 'June',
                 '07': 'July',
                 '08': 'August',
                 '09': 'September',
                 '10': 'October',
                 '11': 'November',
                 '12': 'December'}
        creation_day, creation_month, creation_year = date.split('.')
        return cls(name, id, int(creation_year), month[creation_month], age_restriction)

    def __repr__(self):
        return f"{self.id}: {self.name} ({self.creation_month} " \
               f"{self.creation_year}) has age restriction " \
               f"{self.age_restriction}. " \
               f"Status: {'rented' if self.is_rented else 'not rented'}"
