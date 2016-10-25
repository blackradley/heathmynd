""" Confirm the geohelpers work correctly """

__author__ = "Joe Collins"
__copyright__ = "Copyright (c) 2016 Black Radley Limited."

import unittest
import helpers_geo

class test_geo_helpers(unittest.TestCase):
 
    def setUp(self):
        # set up an array of each test case
        # Name, Link, County, Wiki Location, Google Location
        self.test_data = [

                         ]

        self.test_data = [
                            { # Has wiki text but not geocoded
                                'name': 'Basildon Park',
                                'wikipedia_link': 'Basildon_Park',
                                'county': 'Berkshire',
                                'location_wikipedia': {'lat': 0.0, 'lng': 0.0},
                                'location_google': {'lat': 51.499099,'lng': -1.121399}
                            },
                            { # Has wiki text and is geocoded
                                'name': 'A La Ronde',
                                'wikipedia_link': 'A_La_Ronde',
                                'county': 'Devon', 
                                'location_wikipedia': {'lat': 50.6417, 'lng': -3.4088},
                                'location_google': {'lat': 50.6415663, 'lng': -3.4092041}, 
                            },
                            { # Has wiki text but not geocoded
                                'name': 'Ashdon Museum',
                                'wikipedia_link': 'Ashdon_Museum',
                                'county': 'Essex', 
                                'location_wikipedia': {'lat': 0.0, 'lng': 0.0},
                                'location_google': {'lat': 52.052730, 'lng': 0.310994}, 
                            },
                            { # Has no wiki text at all
                                'name': 'Ariel Centre',
                                'wikipedia_link': 'Ariel_Centre',
                                'county': 'Devon', 
                                'location_wikipedia': {'lat': 0.0, 'lng': 0.0},
                                'location_google': {'lat': 50.4373292, 'lng': -3.6958909}, 
                            },
                            { # the & in the name must be encoded for it to work.
                                'name': 'Kennet & Avon Canal Museum',
                                'wikipedia_link': 'Kennet_&_Avon_Canal_Museum',
                                'county': 'Wiltshire', 
                                'location_wikipedia': {'lat': 51.3552, 'lng': -1.9945},
                                'location_google': {'lat': 51.355174, 'lng': -1.99444  },                        
                            }
        ]
      
    def xxx_test_get_wiki_location(self):
        print '\nWikipedia Location Tests\n---'
        for museum in self.test_data:
            print museum['name'] + ', ' + museum['wikipedia_link']
            location = helpers_geo.get_wikipedia_location(museum['wikipedia_link'])
            self.assertAlmostEqual(location[0], museum['location_wikipedia']['lat'], 4)
            self.assertAlmostEqual(location[1], museum['location_wikipedia']['lng'], 4)
            
    def test_get_google_maps_location(self):
        print '\nGoogle Location Tests\n---'
        for museum in self.test_data:
            print museum['name'] + ', ' + museum['county']
            location = helpers_geo.get_google_location(museum['name'], museum['county'])
            self.assertAlmostEqual(location[0], museum['location_google']['lat'], 4)
            self.assertAlmostEqual(location[1], museum['location_google']['lng'], 4)

if __name__ == '__main__':
    unittest.main()

