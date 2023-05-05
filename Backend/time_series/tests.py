from django.test import TestCase

# Comment: All tests were done manually through the web interface and through curl requests (with files for POST requests)
# Curl requests were done using the following commands:

# curl -X GET http://localhost:8000/_get-solution/
# curl -X GET http://localhost:8000/_get-train-data/
# curl -X POST -H "Content-Type: application/json" --data @./solution.json http://localhost:8000/_solution
# curl -X POST -H "Content-Type: application/json" --data @./train-test.json http://localhost:8000/_upload-data/

# Ideally would have made more sense to create my own test cases, but I don't have much knowledge with this and manually testing didn't take me long
