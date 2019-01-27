# Where is the data from

<http://imd-by-geo.opendatacommunities.org/dimension?area=http://opendatacommunities.org/id/geography/administration/nmd/E07000078>

Store in sqlite3

    C:\>sqlite3 cheltenham
    SQLite version 3.26.0 2018-12-01 12:34:55
    Enter ".help" for usage hints.
    sqlite>
    sqlite> CREATE TABLE code_point (
    ...>     Postcode varchar(7) primary key,
    ...>     Positional_quality_indicator int,
    ...>     Eastings int,
    ...>     Northings int,
    ...>     Country_code varchar(9),
    ...>     NHS_regional_HA_code varchar(9),
    ...> NHS_HA_code varchar(9),
    ...> Admin_county_code varchar(9),
    ...> Admin_district_code varchar(9),
    ...> Admin_ward_code varchar(9)
    ...> );
    sqlite> .mode csv
    sqlite> .import ..\\raw\\cheltenham-code-point.csv code_point
    sqlite> SELECT * FROM code_point LIMIT 5;
    GL1 1AD|10|383316|218534|E92000001|E19000002|E18000010|E10000013|E07000081|E05010967
    GL1 1AE|10|382994|217975|E92000001|E19000002|E18000010|E10000013|E07000081|E05010967
    GL1 1AG|10|383134|218436|E92000001|E19000002|E18000010|E10000013|E07000081|E05010967
    GL1 1AH|10|384609|218051|E92000001|E19000002|E18000010|E10000013|E07000081|E05010955
    GL1 1AJ|50|384609|218051|E92000001|E19000002|E18000010|E10000013|E07000081|E05010955
    sqlite> .quit

    