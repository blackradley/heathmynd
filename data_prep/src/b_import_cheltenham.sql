C:\>sqlite3 cheltenham
SQLite version 3.26.0 2018-12-01 12:34:55
Enter ".help" for usage hints.
sqlite> .mode csv
sqlite> .import ..\\interim\\cheltenham-code-point.csv code_point
sqlite> SELECT * FROM code_point LIMIT 5;
GL11AD,51.86513987,-2.24369579
GL11AE,51.8601041,-2.24834438
GL11AG,51.86425325,-2.24633409
GL11AH,51.86083443,-2.22489638
GL11AJ,51.86083443,-2.22489638
sqlite> .import ..\\interim\\cheltenham-deprivation.csv deprivation
sqlite> SELECT * FROM deprivation LIMIT 5;
GL501AD,18120,6
GL501AF,18120,6
GL501AP,17934,6
GL501BA,18120,6
GL501BB,18120,6
sqlite> CREATE VIEW bar_chart_data As
SELECT * 
FROM code_point INNER JOIN deprivation 
ON code_point.postcode = deprivation.postcode;

sqlite>select * from bar_chart_data LIMIT 5;
GL501AD,51.89363,-2.07739,51.89368,-2.07731,GL501AD,18120,6
GL501AF,51.89367,-2.07701,51.89372,-2.07694,GL501AF,18120,6
GL501AP,51.89692,-2.08046,51.89697,-2.08039,GL501AP,17934,6
GL501BA,51.89634,-2.07674,51.89639,-2.07666,GL501BA,18120,6
GL501BB,51.89639,-2.07485,51.89643,-2.07477,GL501BB,18120,6

sqlite> .output bar_chart_data.csv
sqlite> select * from bar_chart_data
sqlite> .quit
