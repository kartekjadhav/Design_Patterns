from .documentState import DocumentState
from .reviewState import ReviewState

class EditState(DocumentState):
    def edit(self):
        print("Currently in Editing mode")
    
    def review(self):
        print("Moving to reviewing mode")
        return ReviewState()
    
    def finalize(self):
        print("Can't finalize without reviewing")