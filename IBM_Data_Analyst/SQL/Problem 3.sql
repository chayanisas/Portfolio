
--List all case numbers for crimes involving minors (children are not considered minors for the purposes of crime analysis)--

SELECT DISTINCT [Case Number], [Description]
FROM [IBM].[dbo].[CHICAGO_CRIME_DATA]
WHERE [Description] LIKE '%MINOR%'