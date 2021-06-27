# ----------------------------------------------------------------
# REQUESTS Script
#
# Description:
#   File for running certain request commands for manual testing
#   of the back-end services. Automated testing occurs on the
#   test_app.py file.
# ----------------------------------------------------------------
import requests

chatterID1 = '60d7c5d3e753bbe49edef578'
chatterID2 = '60d7c5ede753bbe49edef579'

chatID = '60d7c635e753bbe49edef57a'

# Data to be used in requests
request_data = {
    'chatID': chatID,
}

# Executing request
r = requests.get('http://127.0.0.1:5000/message/retrieve_chat/', data = request_data)

# Printing response
print(r.text)