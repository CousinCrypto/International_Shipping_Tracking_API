from datetime import datetime
import requests
import json
from pprint import pprint



def extract_tracking_info(ressy: dict) -> dict:
    module = ressy.get("module", [{}])[0]

    process_info = module.get("processInfo", {})
    latest_trace = module.get("latestTrace", {})
    detail_list = module.get("detailList", [])

    def ts_to_iso(ts):
        if ts is None:
            return None
        return datetime.utcfromtimestamp(ts / 1000).isoformat() + "Z"

    events = []
    for d in detail_list:
        events.append({
            "timestamp": d.get("time"),
            "time_iso": ts_to_iso(d.get("time")),
            "description": d.get("desc"),
            "standard_description": d.get("standerdDesc"),
            "action_code": d.get("actionCode"),
            "timezone": d.get("timeZone"),
            "node": d.get("group", {}).get("nodeDesc"),
        })

    # Sort oldest → newest
    events.sort(key=lambda x: x["timestamp"] or 0)

    return {
        "tracking_number": module.get("mailNo"),
        "origin_country": module.get("originCountry"),
        "destination_country": module.get("destCountry"),
        "status": module.get("status"),
        "status_description": module.get("statusDesc"),
        "progress_rate": process_info.get("progressRate"),
        "progress_percent": (
            round(process_info.get("progressRate", 0) * 100, 1)
            if process_info.get("progressRate") is not None
            else None
        ),
        "latest_event": {
            "timestamp": latest_trace.get("time"),
            "time_iso": ts_to_iso(latest_trace.get("time")),
            "description": latest_trace.get("desc"),
            "standard_description": latest_trace.get("standerdDesc"),
            "action_code": latest_trace.get("actionCode"),
            "node": latest_trace.get("group", {}).get("nodeDesc"),
        },
        "event_history": events,
        "days_in_transit": module.get("daysNumber"),
    }



def fetch_tracking_numbers ():

  international_tracking_numbers = {
      1: {"item": "Item 1","link": "TRACKING_NUMBER_HERE"},
      2: {"item": "Item 2","link": "TRACKING_NUMBER_HERE"},
      3: {"item": "Item 3","link": "TRACKING_NUMBER_HERE"}
  }

  return international_tracking_numbers


def main():
  international_tracking_numbers = fetch_tracking_numbers ()
  for entry in international_tracking_numbers.values():
      code = entry["link"]
      url = f"https://global.cainiao.com/global/detail.json?mailNos={code}&lang=en-US&language=en-US"
      res = requests.get(url)
      response = res.json()
      pretty_response_data = extract_tracking_info(response)
      pprint(pretty_response_data)






if __name__ == "__main__":
    main()



