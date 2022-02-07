
--Find the total number of crimes recorded in the CRIME table.--
SELECT COUNT([Case Number]) AS [Total Number of Crimes]
  FROM [IBM].[dbo].[CHICAGO_CRIME_DATA]


-- List community areas with per capita income less than 11000. --
SELECT [COMMUNITY AREA NAME], [PER CAPITA INCOME ]
  FROM [IBM].[dbo].[CENSUS_DATA]
  WHERE [PER CAPITA INCOME] < 11000


--List all case numbers for crimes involving minors (children are not considered minors for the purposes of crime analysis)--
SELECT DISTINCT [Case Number], [Description]
  FROM [IBM].[dbo].[CHICAGO_CRIME_DATA]
  WHERE [Description] LIKE '%MINOR%'


-- List all kidnapping crimes involving a child?--
SELECT [Case Number], [Description]
  FROM [IBM].[dbo].[CHICAGO_CRIME_DATA]
  WHERE [Primary Type] = 'KIDNAPPING' AND [Description] LIKE '%CHILD%'


-- What kind of crimes were recorded at schools--
SELECT DISTINCT [Primary Type]
  FROM [IBM].[dbo].[CHICAGO_CRIME_DATA]
  WHERE [Location Description] LIKE '%SCHOOL%'


-- List the average safety score for all types of schools.--
SELECT [Elementary, Middle, or High School], AVG([Safety Score]) as [Average Safety Score] 
  FROM [IBM].[dbo].[CHICAGO_PUBLIC_SCHOOLS]
  GROUP BY [Elementary, Middle, or High School]


-- List 5 community areas with highest % of households below poverty line.--
SELECT DISTINCT TOP 5 pub.[Community Area Name], cen.[PERCENT HOUSEHOLDS BELOW POVERTY]
  FROM [IBM].[dbo].[CHICAGO_PUBLIC_SCHOOLS] pub RIGHT JOIN [IBM].[dbo].[CENSUS_DATA] cen ON pub.[Community Area Number] = cen.[Community Area Number] 
  ORDER BY cen.[PERCENT HOUSEHOLDS BELOW POVERTY] DESC


-- Which community area(number) is most crime prone?--
SELECT TOP 1 [Community Area], COUNT([Case Number]) as [Number of Cases]
  FROM [IBM].[dbo].[CHICAGO_CRIME_DATA]
  GROUP BY [Community Area]
  ORDER BY COUNT([Case Number]) DESC


-- Use a sub-query to find the name of the community area with highest hardship index --
SELECT [COMMUNITY AREA NAME]
  FROM [IBM].[dbo].[CENSUS_DATA]
  WHERE [HARDSHIP INDEX] = ( SELECT MAX([HARDSHIP INDEX]) FROM [IBM].[dbo].[CENSUS_DATA])


-- Use a sub-query to determine the Community Area Name with most number of crimes?--
SELECT [COMMUNITY AREA NAME]
  FROM [IBM].[dbo].[CENSUS_DATA]
  WHERE [Community Area NUMBER] = (
    SELECT TOP 1 crime.[Community Area]
	FROM [IBM].[dbo].[CHICAGO_CRIME_DATA] crime 
	GROUP BY crime.[Community Area]
    ORDER BY COUNT(crime.[Case Number]) DESC)



