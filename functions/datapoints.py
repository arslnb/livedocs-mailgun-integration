from datetime import datetime
from datetime import date
from datetime import timedelta
import json
import requests


def get_stats(args):
    try:
        domain_name = args["service_auth"]["domain_name"]
        api_key = args["service_auth"]["api_key"]

        request_url = "https://api.mailgun.net/v3/%s/stats/total" % domain_name
        event = [args["datapoint"]]

        response = requests.get(
            request_url,
            auth=("api", api_key),
            params={"event": event, "duration": "1m"},
        )
        if str(response.status_code) != "200":
            message = json.loads(response._content)["message"]
            return {"status": "failure", "error": message}
        returned = json.loads(response._content)
        if args["datapoint"] == "failed":
            first_value = returned["stats"][0][event[0]]["permanent"]["total"]
        else:
            first_value = returned["stats"][0][event[0]]["total"]

        return {"status": "success", "data": {"returned_val": str(first_value)}}
    except:
        return {"status": "failure", "error": "unexpected error"}
