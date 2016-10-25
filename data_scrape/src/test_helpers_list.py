""" Confirm the list helpers work correctly """

__author__ = "Joe Collins"
__copyright__ = "Copyright (c) 2016 Black Radley Limited."


"""                 
                         {'file':'List_of_museums_in_Devon.htm', 'the_page':'',
                          'type_column':5, 'rows':116, 
                          'first':'A_La_Ronde', 
                          'first_type': 'Historic house', 'first_type_classified':'Historic',
                          'first_type_icon':'museum',
                          'last':'Yelverton_Paperweight_Centre', 
                          'last_type':'Art', 'last_type_classified':'Arts',
                          'last_type_icon':'convenience'},     
                         {'file':'List_of_museums_in_Dorset.htm', 'the_page':'',
                          'type_column':5, 'rows':69, 
                          'first':'Anvil_Point#Anvil_Point_Lighthouse', 
                          'first_type': 'Maritime', 'first_type_classified':'Transport',
                          'first_type_icon':'rec_bus',
                          'last':'Wolfeton_House',
                          'last_type':'Historic house', 'last_type_classified':'Historic',
                          'last_type_icon':'museum'},
                         {'file': 'List_of_museums_in_Gloucestershire.htm', 'the_page':'',
                          'type_column':5, 'rows':59, 
                          'first':'Acton_Court', 
                          'first_type':'Historic house', 'first_type_classified':'Historic',
                          'first_type_icon':'museum',
                          'last':'Yate_and_District_Heritage_Centre',
                          'last_type':'Local', 'last_type_classified':'Local',
                          'last_type_icon':'govtbldgs'},
                         {'file':'List_of_museums_in_Somerset.htm', 'the_page':'',
                          'type_column':5, 'rows':83,
                          'first':'American_Museum_in_Britain',
                          'first_type':'Art', 'first_type_classified':'Arts', 
                          'first_type_icon':'convenience',
                          'last':'Yeovil_Railway_Centre',
                          'last_type':'Railway', 'last_type_classified':'Transport',
                          'last_type_icon':'rec_bus'}, 
                        {'file':'List_of_museums_in_Wiltshire.htm', 'the_page':'', 
                         'type_column':5, 'rows':55,
                         'first':'Avebury#Alexander_Keiller_Museum', 
                         'first_type':'Archaeology', 'first_type_classified':'Historic',
                         'first_type_icon':'museum',
                         'last':'Wootton_Bassett_Museum',
                         'last_type':'Local', 'last_type_classified':'Local',
                         'last_type_icon':'govtbldgs'},  

"""
import unittest
import helpers_list

class test_list_helpers(unittest.TestCase):
 
    def setUp(self):
        # set up an array of file names and then read all the contents
        # Test filename, Test Data, Number of Columns, Number of Rows, First Link, Last Link
        self.counties = [
                         {'file': 'List_of_museums_in_Cornwall.htm', 'the_page':'',
                          'type_column':5, 'rows':67, 
                          'first':'Antony_House', 
                          'first_type':'Historic house', 'first_type_classified':'Historic',
                          'first_type_icon':'museum',
                          'last':'Wheal_Martyn_China_Clay_Country_Park',
                          'last_type':'Industry', 'last_type_classified':'Industrial',
                          'last_type_icon':'factory'},
 
                        ]
        for county in self.counties:
            county['the_page'] = open('../download/' + county['file'], "r").read()
                 
    def test_get_museum_type_column(self):
        print 'test_get_museum_type_column'
        for county in self.counties:
            the_page = county['the_page']
            type_column_number = helpers_list.get_museum_type_column(the_page)
            print '\t' + county['file']
            self.assertEqual(type_column_number, county['type_column'])
            
    def XX_test_get_museums_list(self):
        print 'test_get_museums_list'
        for county in self.counties:
            the_page = county['the_page']
            museums = helpers_list.get_museums_list(the_page)
            print '\t' + county['file']
            # Check number of rows
            self.assertEqual(len(museums), county['rows'])
            # Check first
            self.assertEqual(museums[0][1], county['first'])
            # Check last
            self.assertEqual(museums[len(museums)-1][1], county['last'])
    
    def XX_test_get_museum_types(self):
        print 'test_get_museum_types'
        for county in self.counties:
            print '\t' + county['file']
            the_page = county['the_page']
            type_column = county['type_column']
            types = helpers_list.get_museum_types(the_page, type_column)
            # Check first
            self.assertEqual(types[0], county['first_type'])
            # Check last
            self.assertEqual(types[len(types)-1], county['last_type'])
            
    def XX_test_classify_type(self):
        print 'test_classify_type'
        for county in self.counties:
            print '\t' + county['file']
            # Check first classified
            type = county['first_type']
            classified_type = helpers_list.classify_type(type)
            self.assertEqual(classified_type, county['first_type_classified'])
            # Check last classified
            type = county['last_type']
            classified_type = helpers_list.classify_type(type)
            self.assertEqual(classified_type, county['last_type_classified'])
            
    def XX_test_iconize_type(self):
        print 'test_iconize_type'
        for county in self.counties:
            print '\t' + county['file']
            # Check first icon
            type = county['first_type']
            classified_type = helpers_list.classify_type(type)
            icon = helpers_list.iconize_type(classified_type)
            self.assertEqual(icon, county['first_type_icon'])
            # Check last icon
            type = county['last_type']
            classified_type = helpers_list.classify_type(type)
            icon = helpers_list.iconize_type(classified_type)
            self.assertEqual(icon, county['last_type_icon'])
       
if __name__ == '__main__':
    unittest.main()
   


