import requests
import os
import logging

class VansahBinding:
    apiVersion = 'v1'
    Vansah_URL = "https://prod.vansahnode.app"

    @staticmethod
    def sendResultsToVansah(TestCaseKey, AssetKey, Result):
        runPath = f'/api/{VansahBinding.apiVersion}/run'
        endpoint = VansahBinding.Vansah_URL + runPath

        payload = {
            "case": {"key": TestCaseKey},
            "asset": {"type": "issue", "key": AssetKey},
            "result": {"name": Result}
        }

        # Construct request headers
        headers = {
            "Authorization": os.environ.get("VANSAH_TOKEN"),
            "Content-Type": "application/json"
        }

        logging.info("Sending payload to Vansah: %s", payload)
        response = requests.post(endpoint, headers=headers, json=payload)
        logging.info("Vansah response: %s", response.text)

        return response.text
