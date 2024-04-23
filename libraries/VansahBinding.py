import requests

class VansahBinding:

    apiVersion = 'v1'
    runPath = '/api/run'

    def __init__(self,Vansah_URL):
        self.Vansah_URL = Vansah_URL
        self.endpoint = Vansah_URL+self.apiVersion+self.runPath
    
    def sendResultstoVansah(self,TestCaseKey,AssetKey):
        self.TestCaseKey = TestCaseKey
        self.AssetKey = AssetKey

    def vansahRunAPI(self):
        response = requests.post(self.endpoint,json={})
        return response
    