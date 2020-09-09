import os
import sys
from typing import Any, Dict, List, Union, NoReturn, Optional, Callable
from numbers import Real
from settings import logger, env
import utils
import requests
from flask import jsonify, Response
import json


class Pharmacy:

    @classmethod
    def SearchNearestPharmacy(cls, currentLocation: Dict, range: int, limit: int) -> dict:
        uri = env("DATA_URL")
        try:
            res = requests.get(uri)
        except requests.ConnectionError:
            logger.error("Connection error")
            return utils.createResponse(503, "Connection Error")
        except Exception as e:
            logger.error(str(e))
            return utils.createResponse(500, str(e))
        if res.status_code != 200:
            logger.error(res.status_code)
            return utils.createResponse(res.status_code, "Service error")
        # logger.warning(json.dumps(res.json()))
        data = res.json()['features']
        return utils.createResponse(res.status_code, "OK")
