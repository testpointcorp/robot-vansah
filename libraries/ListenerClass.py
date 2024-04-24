from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn
import requests
import os
import logging

class ListenerClass:
    ROBOT_LISTENER_API_VERSION = 3
    ROBOT_LIBRARY_SCOPE = "GLOBAL"

    def end_test(self, data, result):
        variables = BuiltIn().get_variables()  # Get all test case variables
        logger.info(f"Test case variables: {variables}")
        print(f"Test case variables: {variables}")

        # Extract AssetKey and TestCaseKey values
        asset_key = variables.get('${AssetKey}', '').strip('"')
        test_case_key = variables.get('${TestCaseKey}', '').strip('"')

        logger.info(f"AssetKey: {asset_key}")
        logger.info(f"TestCaseKey: {test_case_key}")
        logger.info(f"Test status: {result.status}")

        # Ensure the sendResultsToVansah method is called with correct arguments
        try:
            response = self.sendResultsToVansah(self,test_case_key, asset_key, result.status)
            logger.info(f"Vansah response: {response}")
        except AttributeError as e:
            logger.error(f"Error accessing self.sendResultsToVansah: {e}")
            raise

        print(f"Vansah response: {response}")
    
    apiVersion = 'v1'
    Vansah_URL = "https://prod.vansahnode.app"

    def sendResultsToVansah(self,TestCaseKey, AssetKey, Result):
        runPath = f'/api/{self.apiVersion}/run'
        endpoint = self.Vansah_URL + runPath
        vansahResult = "passed"
        if Result != "PASS":
            vansahResult = "failed"
        payload = {
            "case": {"key": TestCaseKey},
            "asset": {"type": "issue", "key": AssetKey},
            "result": {"name": vansahResult}
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