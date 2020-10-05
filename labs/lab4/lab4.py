import urllib.parse
import http.client
import time

key = "54CDA6FJF4RCJ92C"  # Put your API Key here


def lab4():
    email = "baileylyster@cmail.carleton.ca"
    myLetter = "C"
    myGroup = "L2-M-10"

    params = urllib.parse.urlencode(
        {"field1": email, "field2": myGroup, "field3": myLetter, "key": key}
    )
    headers = {
        "Content-typZZe": "application/x-www-form-urlencoded",
        "Accept": "text/plain",
    }
    conn = http.client.HTTPConnection("api.thingspeak.com:80")
    try:
        conn.request("POST", "/update", params, headers)
        response = conn.getresponse()
        print(response.status, response.reason)
        conn.close()
    except:
        print("connection failed")


if __name__ == "__main__":
    lab4()
