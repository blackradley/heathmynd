# Where is the data from

<http://imd-by-geo.opendatacommunities.org/dimension?area=http://opendatacommunities.org/id/geography/administration/nmd/E07000078>

Store in sqlite3

C:\>sqlite3 cheltenham
SQLite version 3.26.0 2018-12-01 12:34:55
Enter ".help" for usage hints.
sqlite>

.mode csv
.import ..\\raw\\cheltenham-code-point.csv code_point
SELECT * FROM code_point LIMIT 5;

"GL1 1AD",10,383316,218534,E92000001,E19000002,E18000010,E10000013,E07000081,E05010967
"GL1 1AE",10,382994,217975,E92000001,E19000002,E18000010,E10000013,E07000081,E05010967
"GL1 1AG",10,383134,218436,E92000001,E19000002,E18000010,E10000013,E07000081,E05010967
"GL1 1AH",10,384609,218051,E92000001,E19000002,E18000010,E10000013,E07000081,E05010955
"GL1 1AJ",50,384609,218051,E92000001,E19000002,E18000010,E10000013,E07000081,E05010955

.import ..\\raw\\cheltenham-deprivation.csv deprivation

SELECT * FROM deprivation LIMIT 5;

"GL50 1AA",Terminated,E01022153,"Cheltenham 004D E01022153",6686,3
"GL50 1AD",Live,E01022117,"Cheltenham 009B E01022117",18120,6
"GL50 1AE",Terminated,E01022152,"Cheltenham 004C E01022152",2413,1
"GL50 1AF",Live,E01022117,"Cheltenham 009B E01022117",18120,6
"GL50 1AP",Live,E01022126,"Cheltenham 009F E01022126",17934,6

sqlite> .quit

    