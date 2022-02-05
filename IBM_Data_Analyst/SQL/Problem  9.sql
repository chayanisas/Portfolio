
-- Use a sub-query to find the name of the community area with highest hardship index --
SELECT [COMMUNITY AREA NAME]
FROM [IBM].[dbo].[CENSUS_DATA]
WHERE [HARDSHIP INDEX] = ( SELECT MAX([HARDSHIP INDEX]) FROM [IBM].[dbo].[CENSUS_DATA])