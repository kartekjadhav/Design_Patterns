from .Handler import AnimalHandler

class BearHandler(AnimalHandler):
    def set_next(self, handler):
        self._next_handler = handler
        return self._next_handler

    def handle(self, value:str):
        if value == 'Fish':
            return 'Bear'
        elif self._next_handler != None:
            return self._next_handler.handle(value)
        else:
            return None