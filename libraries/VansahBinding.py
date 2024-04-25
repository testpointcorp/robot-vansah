import requests
import os

class VansahBinding:
    apiVersion = 'v1'
    Vansah_URL = "https://prod.vansahnode.app"  #By default
    
    def setVansahURL(self,Vansah_URL):  #To update the Vansah URL, if Vansah is pinned to other than US location
        self.Vansah_URL = Vansah_URL

    def sendResultsToVansah(self,TestCaseKey, AssetKey, Result,Properties):   #To send API request to Vansah to execute the Test Case
        runPath = f'/api/{self.apiVersion}/run'
        endpoint = self.Vansah_URL + runPath
        vansahResult = "passed"

        if Result != "PASS":
            vansahResult = "failed"

        payload = {
            "case": {"key": TestCaseKey},
            "asset": self.assetObject(AssetKey),
            "result": {"name": vansahResult},
            "properties":Properties
        }
     
        # Construct request headers
        headers = {
            "Authorization": os.environ.get("VANSAH_TOKEN"),
            "Content-Type": "application/json"
        }
        response = requests.post(endpoint, headers=headers, json=payload)
        return response.text

    def propertiesObject(self,SprintName, ReleaseName, EnvironmentName):
        properties = {}
        if(SprintName):
            properties['sprint'] = {"name" : SprintName}
        if(ReleaseName):
            properties['release'] = {"name" : ReleaseName}    
        if(EnvironmentName):
            properties['environment'] = {"name" : EnvironmentName}

        return properties
    
    def assetObject(self,AssetKey):
        AssetObject = {}

        if(self.isIssueKey(AssetKey)):
            AssetObject['type'] = "issue"
            AssetObject["key"] = AssetKey
        else:
            AssetObject['type'] = "folder"
            AssetObject["identifier"] = AssetKey              

        return AssetObject
    
    def isIssueKey(self,AssetKey):
        count = AssetKey.count("-")
        if(count>1):
            return False
        return True