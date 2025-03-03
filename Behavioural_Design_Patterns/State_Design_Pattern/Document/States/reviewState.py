from .documentState import DocumentState
from .finalizeState import FinalizeState

class ReviewState(DocumentState):
    def edit(self):
        print("Document in reviewing state. Editing not allowed")
    
    def review(self):
        print("Document in reviewing state")
    
    def finalize(self):
        print("Moving to finalize state")
        return FinalizeState()