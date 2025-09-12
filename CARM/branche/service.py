import requests
BASE_URL = "https://api.postalpincode.in/pincode/"

def get_pincode(pincode: str):
    try:
        response = requests.get(BASE_URL + str(pincode), timeout=10)
        response.raise_for_status()  # raise error for bad HTTP status
        data = response.json()
        
        if data and data[0]["Status"] == "Success":
            post_offices = data[0]["PostOffice"]
            return [
                {
                    "Name": po["Name"],
                    "District": po["District"],
                    "State": po["State"],
                    "Country": po["Country"]
                }
                for po in post_offices
            ]
        else:
            return f"No details found for pincode {pincode}"
    except Exception as e:
        return f"Error: {str(e)}"