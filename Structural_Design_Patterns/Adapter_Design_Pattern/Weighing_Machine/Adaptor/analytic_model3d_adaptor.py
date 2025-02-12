from .adaptor import Adaptor

class AnalyticModel3DAdaptor(Adaptor):
    def __init__(self):
        super().__init__()
    def createModel(self, data):
        if isinstance(data, str) and data == "XML":
            print("Converting to JSON format...")
            data = "JSON"
        elif isinstance(data, str) and data == "JSON":
            print("Data already in JSON format")
        else:
            raise ValueError("Unsupported data format")
        return self._analyticModel3d.createModel(data)