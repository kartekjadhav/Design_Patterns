from document import Document
import States
from inspect import isabstract, getmembers, isclass

if __name__ == "__main__":
    state_members = getmembers(States, lambda m: isclass(m) and not isabstract(m) and issubclass(m, States.DocumentState))
    states = {key:value() for key, value in state_members}
    print("States available:- ")
    for key in states.keys():
        print(key)

    document = Document()
    document.edit_doc()
    document.finalize_doc()
    document.review_doc()

    document.edit_doc()
    document.review_doc()
    document.finalize_doc()

    document.edit_doc()
    document.review_doc()
    document.finalize_doc()

    value = input("Enter state to change - ").strip();
    document.set_state(states[value])
    document.getState()

    document.edit_doc()
    document.finalize_doc()
    document.review_doc()

    document.edit_doc()
    document.review_doc()
    document.finalize_doc()

    document.edit_doc()
    document.review_doc()
    document.finalize_doc()