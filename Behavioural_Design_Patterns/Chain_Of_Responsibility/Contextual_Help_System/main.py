from Handlers import Dialog, Panel, OkButton, CancelButton

class Application():
    def __init__(self):
        self.dialog = None
        self.panel = None
        self.okButton = None
        self.cancelButton = None
    
    def buildGUI(self):
        self.dialog = Dialog("http://example.com/wiki/BudgetReports")
        self.panel = Panel("This panel displays budget reports.")
        self.okButton = OkButton("This is an OK button that confirms the action.")
        self.cancelButton = CancelButton("This is a Cancel button that confirms the action.")

        self.panel.add_child(self.cancelButton)
        self.panel.add_child(self.okButton)
        self.dialog.add_child(self.panel)
    
    def on_press_F1_button(self, component):
        print(f"F1 has been pressed on {component.__class__.__name__}")
        component.help()

if __name__ == "__main__":
    app = Application()
    app.buildGUI()

    app.on_press_F1_button(app.okButton)
    app.on_press_F1_button(app.cancelButton)
    app.on_press_F1_button(app.panel)
    app.on_press_F1_button(app.dialog)