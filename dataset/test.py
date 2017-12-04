from django.test import TestCase
from dataset.views import convert_province_abbr_to_name

class ProvinceAbbrTestCase(TestCase):

    def test_convert_province_abbr_to_name(self):
        self.assertEqual(convert_province_abbr_to_name("ON"), "Ontario")
        self.assertEqual(convert_province_abbr_to_name("NL"), "Newfoundland and Labrador")
        self.assertEqual(convert_province_abbr_to_name("QC"), "Quebec")
        self.assertEqual(convert_province_abbr_to_name("NS"), "Nova Scotia")
