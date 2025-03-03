from .documentState import DocumentState

class FinalizeState(DocumentState):
    def edit(self):
        print("Document in finalizing state. Editing not allowed")
    
    def review(self):
        print("Document is finalized. Reviewing not allowed")
    
    def finalize(self):
        print("Document is already finalized")