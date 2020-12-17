from Person import Person
import json


class PersonEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Person):
            return o.asdict()

        return super().default(o)(self, o)
