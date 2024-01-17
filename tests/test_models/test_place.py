#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import TestBaseModel
from models.place import Place


class TestPlace(TestBaseModel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_place_attributes(self):
        """ """
        place = self.value()
        attributes = [
            "city_id",
            "user_id",
            "name",
            "description",
            "number_rooms",
            "number_bathrooms",
            "max_guest",
            "price_by_night",
            "latitude",
            "longitude",
            "amenity_ids"
        ]

        for attribute in attributes:
            self.assertTrue(hasattr(place, attribute))
            if type(getattr(place, attribute)) == str:
                self.assertEqual(type(getattr(place, attribute)), str)
            elif type(getattr(place, attribute)) == int:
                self.assertEqual(type(getattr(place, attribute)), int)
            elif type(getattr(place, attribute)) == float:
                self.assertEqual(type(getattr(place, attribute)), float)
            elif type(getattr(place, attribute)) == list:
                self.assertEqual(type(getattr(place, attribute)), list)
