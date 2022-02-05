
-- List all kidnapping crimes involving a child?--

SELECT [Case Number], [Description]
FROM [IBM].[dbo].[CHICAGO_CRIME_DATA]
WHERE [Primary Type] = 'KIDNAPPING' AND [Description] LIKE '%CHILD%'
