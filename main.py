# Define start and end dates for event and station searches
START = "2020-01-01"
END = "2020-06-01"

# Define event minimum magnitude
MAG_MIN = 5

# Define the bounding box for event and station searches
LAT_MIN = 40
LAT_MAX = 45
LON_MIN = 17
LON_MAX = 25

# Max radius of stations from the epicenter
RADIUS_MAX = 2

# Encoding for HTTP requests
ENCODING = "utf-8"

# ------------------------------------------------------------------------------

import requests
from obspy.clients.fdsn.client import Client
from obspy.clients.fdsn import RoutingClient

client_gfz = Client("GFZ")
client_eida = RoutingClient("eida-routing")

# ------------------------------------------------------------------------------

catalog = client_gfz.get_events(
    starttime=START,
    endtime=END,
    minmagnitude=MAG_MIN,
    minlatitude=LAT_MIN,
    maxlatitude=LAT_MAX,
    minlongitude=LON_MIN,
    maxlongitude=LON_MAX,
)

event = catalog[0]

# ------------------------------------------------------------------------------

inventory = client_eida.get_stations(
    startbefore=event.origins[0].time,
    endafter=event.origins[0].time,
    latitude=event.origins[0].latitude,
    longitude=event.origins[0].longitude,
    maxradius=RADIUS_MAX,
)

print(inventory)

# ------------------------------------------------------------------------------
event_day = event.origins[0].time.strftime("%Y-%m-%d")

required_channels = {
    "BH?": ["BHE", "BHN", "BHZ"],
    "HH?": ["HHE", "HHN", "HHZ"],
    "LH?": ["LHE", "LHN", "LHZ"],
}

for net in inventory.networks:
    for sta in net.stations:
        wfcatalog_url = "http://eida-federator.ethz.ch/eidaws/wfcatalog/1/query"

        query_params = {
            "start": event_day,
            "end": event_day,
            "network": net.code,
            "station": sta.code,
            "max_gap": 0,
            "max_overlap": 0,
            "percent_availability": 100
        }

        # Request the data...
        r = requests.get(wfcatalog_url, params=query_params, timeout=10)
        r.encoding = ENCODING

        if r.status_code == 200:
            pass
        else:
            pass

# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
