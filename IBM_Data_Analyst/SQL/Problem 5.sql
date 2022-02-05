
-- What kind of crimes were recorded at schools--

SELECT DISTINCT [Primary Type]
FROM [IBM].[dbo].[CHICAGO_CRIME_DATA]
WHERE [Location Description] LIKE '%SCHOOL%'


