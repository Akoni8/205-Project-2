import json

def get_room(id):
    ret = None
    with open(str(id)+ ".json", "r") as f:
        jsontext = f.read()
        d = json.loads(jsontext)
        d['id'] = id
        ret = Room(**d)
        return ret
class Room():
    """Rooms"""
    def __init__(self,id=0, name="A room", description="An empty room", neighbors={}):
        self.id = id
        self.name = name
        self.description = description
        self.neighbors = neighbors

    def _neighbors(self, direction):
        if direction in self.neighbors:
            return self.neighbors[direction]
        else:
            return None
    def north(self):
        return self._neighbors('n')

    def south(self):
        return self._neighbors('s')

    def east(self):
        return self._neighbors('e')

    def west(self):
        return self._neighbor('w')


