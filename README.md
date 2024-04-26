# Robot Framework Integration with Vansah Test Management For Jira
This tutorial guides you through the process of integrating Robot Framework with Vansah Test Management for Jira to automatically send your test case results.

By following this setup, you can streamline your testing workflow, ensuring that test outcomes are recorded directly in your Jira workspace.
## Prerequisites
- Robot Framework - [Test](https://robotframework.org/#getting-started) project is already setup.
- Make sure that [`Vansah`](https://marketplace.atlassian.com/apps/1224250/vansah-test-management-for-jira?tab=overview&hosting=cloud) is installed in your Jira workspace
- You need to Generate **Vansah** [`connect`](https://docs.vansah.com/docs-base/generate-a-vansah-api-token-from-jira-cloud/) token to authenticate with Vansah APIs.
## Configuration
**Setting Environment Variables** - Store your Vansah API token as an environment variable for security. 

For Windows (use cmd)
```cmd
setx VANSAH_TOKEN "your_vansah_api_token_here"

```
For macOS
```bash
echo export VANSAH_TOKEN="your_vansah_api_token_here" >> ~/.bash_profile

source ~/.bash_profile

```
For Linux (Ubuntu, Debian, etc.)
```bash
echo export VANSAH_TOKEN="your_vansah_api_token_here" >> ~/.bashrc

source ~/.bashrc

``` 

## Implementation
To enable Vansah Integration in Robot Framework project, follow these steps:

### Create Variables for Tests

1.  ${AssetKey} is required to declare under variables section - can be empty
2.  ${TestCaseKey} is required to declare under variables section - can be empty
3.  ${SprintName}, ${ReleaseName} and ${EnvironmentName} Test Run properties values are optional. 

```js
*** Variables ***
${AssetKey}    Test-3
${TestCaseKey}
${SprintName}    SM Sprint 1
${ReleaseName}    Release 24
${EnvironmentName}    UAT
```

Note : Variables are case sensitive

### Add `Set Test Variable` in each of your Test Cases

```js
*** Test Cases ***

Open Google Search Page 1
    Open Browser To view Google Page
    [Teardown]    Close Browser
    Set Test Variable    ${TestCaseKey}    Test-C10  //This is required
    Set Test Variable    ${AssetKey}    Test-3      //This is required
```

### Add [`ListenerClass.py`](/libraries/ListenerClass.py) and [`VansahBinding.py`](/libraries/VansahBinding.py) to your libraries folder

If your Vansah is pinned to any other location than US, please use : 
```js
//ListenerClass.py

        vansahBind = VansahBinding()
        
        // After line number : 18 in your ListenerClass.py add below code to update the Vansah URL

        vansah.setVansahURL("Add your Vansah Connect URL")
        
```

### Running your Test with the ListenerClass.py
Use below command to run your tests
```cmd
robot --listener .\libraries\ListenerClass.py test
```

Output : `Vansah Response : A new Test Run created.`

```js
C:\Users\onesh\..\GitHub\robot-vansah> robot --listener .\libraries\ListenerClass.py test
==============================================================================
Test
==============================================================================
Test.Testsuite Functional
==============================================================================
Open Google Search Page 1
DevTools listening on ws://127.0.0.1:51936/devtools/browser/6dba13bd-1197-4656-96a7-1d13dbdc67d8
....
 Vansah Response : A new Test Run created.
Open Google Search Page 1                                             | PASS |
------------------------------------------------------------------------------
Open Google Search Page 2
DevTools listening on ws://127.0.0.1:51961/devtools/browser/ae132c3b-50ab-4560-b85b-c2b08960a157
....
 Vansah Response : A new Test Run created.
Open Google Search Page 2                                             | PASS |
------------------------------------------------------------------------------
Test.Testsuite Functional                                             | PASS |
2 tests, 2 passed, 0 failed
==============================================================================
Test                                                                  | PASS |
2 tests, 2 passed, 0 failed
```

### Conclusion
By following the above steps, your Robot Framework project will be equipped to send test run results directly to Vansah, streamlining your testing and reporting process.

Ensure that all files are placed and configured as described to facilitate successful integration.

For more details on Robot Framework, visit the [docs](https://robotframework.org/#getting-started).

For Vansah specific configurations and API details, please refer to the [Vansah API documentation](https://apidoc.vansah.com/).
