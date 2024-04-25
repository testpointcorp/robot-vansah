import json
from robot.libraries.BuiltIn import BuiltIn
from VansahBinding import VansahBinding

class ListenerClass:
    ROBOT_LISTENER_API_VERSION = 3
    ROBOT_LIBRARY_SCOPE = "GLOBAL"

    def end_test(self, data,result):
        variables = BuiltIn().get_variables()  # Get all test case variables
        
        # Extract AssetKey and TestCaseKey values
        asset_key = variables.get('${AssetKey}', '').strip('"')
        test_case_key = variables.get('${TestCaseKey}', '').strip('"')

        # Calling sendResultsToVansah method
        try:
            vansahBind = VansahBinding()

            # Assigning Test Run Properties
            SprintName = variables.get('${SprintName}', '').strip('"')
            ReleaseName = variables.get('${ReleaseName}', '').strip('"')
            EnvironmentName = variables.get('${EnvironmentName}', '').strip('"')
            Properties = vansahBind.propertiesObject(SprintName,ReleaseName,EnvironmentName)

            response = json.loads(vansahBind.sendResultsToVansah(test_case_key, asset_key, result.status,Properties))
            message_text = response.get('message')
            print(f"\n Vansah Response : {message_text}")
        except AttributeError as e:
            print(f"\n Listener Response : {e}")
            raise   