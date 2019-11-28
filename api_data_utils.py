''' File: api_data_utils.py '''
import sys
import requests
import json

import numpy as np
import pandas as pd
from pandas.io.json import json_normalize

# Hit the API and handle HTTPError exception (i.e. 404)


def fetch_and_parse_json():
    try:
        res = requests.get(
            'https://api.coastal.ca.gov/vulnerability/v1/counties')
        res.raise_for_status()
        parsed_json = json_normalize(res.json())
    except requests.exceptions.HTTPError as err:
        print(err)
        sys.exit(1)
    # TODO: Add except blocks for ConnectionException and Timeout
    else:
        return parsed_json
