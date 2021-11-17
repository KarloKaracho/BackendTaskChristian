# BackendTaskChristian

How to deploy and test?
----------------
- the master branch is connected to Heroku and is automatically deployed, meaning that it would be better to develop within a dedicated development branch and merge the branches for a final release. 
- before branches get merged, make sure all dependencies are within the requirements.txt file: pip freeze > requirements.txt
- make sure you have selected the right python version within the runtime.txt file: python -V
- set the right database password on the appropriate place holder
- Perform an integration test using Postman after you merged the branches and therefore deployed the application. It might be beneficial to use a dedicated test server in order to perform the integration test first before it gets commited to the actual platform. Make sure all test are integrated and tested locally using the JSON-file within the tests subfolder integration_test. This test is necessary even if you performed equivalent unit tests.


