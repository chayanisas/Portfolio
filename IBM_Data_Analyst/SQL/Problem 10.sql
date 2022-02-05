
-- Use a sub-query to determine the Community Area Name with most number of crimes?--

SELECT [COMMUNITY AREA NAME]
FROM [IBM].[dbo].[CENSUS_DATA]
WHERE [Community Area NUMBER] = (
    SELECT TOP 1 crime.[Community Area]
	FROM [IBM].[dbo].[CHICAGO_CRIME_DATA] crime 
	GROUP BY crime.[Community Area]
    ORDER BY COUNT(crime.[Case Number]) DESC)