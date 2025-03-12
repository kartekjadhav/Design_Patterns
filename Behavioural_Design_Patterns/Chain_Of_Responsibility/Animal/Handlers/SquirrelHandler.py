from .Handler import AnimalHandler

class SquirrelHandler(AnimalHandler):
    def set_next(self, handler):
        self._next_handler = handler
        return self._next_handler

    def handle(self, value:str):
        if value == 'Nuts':
            return 'Squirrel'
        elif self._next_handler != None:
            return self._next_handler.handle(value)
        else:
            return None