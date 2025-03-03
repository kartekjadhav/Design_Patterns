from States import DocumentState, EditState

class Document:
    def __init__(self):
        self._state = EditState()
    
    def set_state(self, state:DocumentState):
        self._state = state
    
    def edit_doc(self):
        self._state.edit()
    
    def review_doc(self):
        state = self._state.review()
        if state:
            self.set_state(state)

    def finalize_doc(self):
        state = self._state.finalize()
        if state:
            self._state = state
    
    def getState(self):
        print(f"{self._state}")