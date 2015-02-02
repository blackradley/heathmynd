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
                           [0.0, 0.0], [51.4994454, -1.121161]], # Has wiki text but no geocoded
                          ['A La Ronde', 'A_La_Ronde', 'Devon', 
                           [50.6417, -3.4088], [50.6428, -3.4055]], # Has wiki text and is geocoded
                          ['Ariel Centre', 'Ariel_Centre', 'Devon', 
                           [0.0, 0.0], [50.7772135, -3.9994610]], # Has no wiki text at all
                          ['Kennet & Avon Canal Museum', 'Kennet_&_Avon_Canal_Museum', 'Wiltshire', 
                           [51.3552, -1.9945], [51.2462714, -1.9922127]] # the & in the name must be encoded for it to work.
                         ]
         
    def test_get_wiki_location(self):
        print 'Wikipedia Location Tests'
        for museum in self.test_data:
            location = helpers_geo.get_wiki_location(museum[1])
            print museum[0] + str(location)
            self.assertEqual(location, museum[3])
            
    def test_get_google_location(self):
        print 'Google Location Tests' 
        for museum in self.test_data:
            location = helpers_geo.get_google_location(museum[0], museum[2])
            print museum[0] + str(location)
            self.assertEqual(location, museum[4])
            