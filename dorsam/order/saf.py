import requests

headers = {

  'Content-Type': 'application/json',

  'Authorization': 'Bearer zrwqlEm1PG3nlt2AX1Ex6cRLvVrF'

}

payload = {

    "BusinessShortCode": 174379,

    "Password": "MTc0Mzc5YmZiMjc5ZjlhYTliZGJjZjE1OGU5N2RkNzFhNDY3Y2QyZTBjODkzMDU5YjEwZjc4ZTZiNzJhZGExZWQyYzkxOTIwMjIwODI4MjAzMjU1",

    "Timestamp": "20220828203255",

    "TransactionType": "CustomerPayBillOnline",

    "Amount": 1,

    "PartyA": 254708374149,

    "PartyB": 174379,

    "PhoneNumber": 254708374149,

    "CallBackURL": "https://mydomain.com/path",

    "AccountReference": "CompanyXLTD",

    "TransactionDesc": "Payment of X" 

  }

response = requests.request("POST", 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest', headers = headers, data = payload)

print(response.text.encode('utf8'))