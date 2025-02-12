class AnalyticModel3D():
    def createModel(self, data):
        print(f"Recieved data of type - {data}")
        if data == 'JSON':
            return "Your model has been created => :D :D :D"
        else:
            raise Exception("Can only process JSON data")