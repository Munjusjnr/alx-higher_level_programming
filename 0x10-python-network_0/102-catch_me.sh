#!/bin/bash
# script that makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message in the body of a response
curl -s -L -X PUT -H "Origin: School" -d "user_id=98" 0.0.0.0:5000/catch_me
