
-- Which community area(number) is most crime prone?--


SELECT TOP 1 [Community Area], COUNT([Case Number]) as [Number of Cases]
FROM [IBM].[dbo].[CHICAGO_CRIME_DATA]
GROUP BY [Community Area]
ORDER BY COUNT([Case Number]) DESC
