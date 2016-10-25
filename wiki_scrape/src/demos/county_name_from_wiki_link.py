'''
Get the county name from the end of a wiki link.

Joe Collins
26 March 2011

'''
import string
county_link = 'List_of_museums_in_Bedfordshire'
print string.split(county_link, '_')[-1]
raw_input("Press ENTER to exit")
