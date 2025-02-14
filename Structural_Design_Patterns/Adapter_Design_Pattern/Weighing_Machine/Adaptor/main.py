from Adaptor import AnalyticModel3DAdaptor

analyticModel3dAdaptor = AnalyticModel3DAdaptor()

try:
    model = analyticModel3dAdaptor.createModel("CSV")
    print(model)
except Exception as e:
    print(e)