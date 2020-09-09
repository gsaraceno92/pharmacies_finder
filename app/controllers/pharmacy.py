import os
import sys
from typing import Any, Dict, List, Union, NoReturn, Optional, Callable
from numbers import Real
from settings import logger, env
import utils
import requests
from flask import jsonify
import json
import operator


class Pharmacy:

    @classmethod
    def SearchNearestPharmacy(cls, currentLocation: Dict, range: int, limit: int) -> tuple:
        if not {"latitude", "longitude"} <= currentLocation.keys():
            return utils.createResponse(422, "Validation error: currentLocation must contain 'latitude' and 'longitude'")

        uri = env("DATA_URL")
        try:
            res = requests.get(uri, timeout=1)
        except requests.ConnectionError:
            logger.error("Connection error")
            return {"message": "Connection Error"}, 503
        except Exception as e:
            logger.error(str(e))
            return {"message": str(e)}, 500
        if res.status_code != 200:
            logger.error(res.status_code)
            return {"message": "Service error"}, res.status_code

        data = res.json()['features']
        pharmacies_distance = []

        for key, pharmacy in enumerate(data):
            coordinates = pharmacy['geometry']['coordinates']
            pharmacy_name = pharmacy['properties']['Descrizione']
            distance = utils.haversine_distance(currentLocation['latitude'], currentLocation['longitude'], coordinates[1], coordinates[0])
            pharmacies_distance.append({
                "name": pharmacy_name,
                "distance": distance,
                "location": {
                    "latitude": coordinates[1],
                    "longitude": coordinates[0]
                }
            })
        sorted_pharmacies = sorted(pharmacies_distance,  key=lambda k: k['distance'])
        sorted_pharmacies = sorted_pharmacies[:limit] if limit < len(sorted_pharmacies) else sorted_pharmacies 
        return {
            "pharmacies": sorted_pharmacies
        }, 200
