'''
Confirm the geohelpers work correctly

Joe J Collins
31 March 2011
'''
import unittest
import helpers_geo

class test_geo_helpers(unittest.TestCase):
    '''
    '''    
    def setUp(self):
        # set up an array of each test case
        # Name, Link, County, Wiki Location, Google Location
        self.test_data = [
                          ['Basildon Park', 'Basildon_Park', 'Berkshire', 
                           [0.0, 0.0], [51.4994454, -1.121161]], # Has wiki text but not geocoded
                          ['A La Ronde', 'A_La_Ronde', 'Devon', 
                           [50.6417, -3.4088], [50.6428, -3.4055]], # Has wiki text and is geocoded
                          ['Ashdon Museum', 'Ashdon_Museum', 'Essex', 
                           [0.0, 0.0], [52.052730, 0.310994]], # Has wiki text but not geocoded
                          ['Ariel Centre', 'Ariel_Centre', 'Devon', 
                           [0.0, 0.0], [50.7772135, -3.9994610]], # Has no wiki text at all
                          ['Kennet & Avon Canal Museum', 'Kennet_&_Avon_Canal_Museum', 'Wiltshire', 
                           [51.3552, -1.9945], [51.2462714, -1.9922127]] # the & in the name must be encoded for it to work.
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
                                'location_google': {'lat': 50.7155591, 'lng': -3.4092041}, 
                            }
        ]
      
    def test_get_wiki_location(self):
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