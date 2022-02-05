
-- List 5 community areas with highest % of households below poverty line.--
SELECT DISTINCT TOP 5 pub.[Community Area Name], cen.[PERCENT HOUSEHOLDS BELOW POVERTY]
  
  FROM [IBM].[dbo].[CHICAGO_PUBLIC_SCHOOLS] pub RIGHT JOIN [IBM].[dbo].[CENSUS_DATA] cen ON pub.[Community Area Number] = cen.[Community Area Number] 
  
  ORDER BY cen.[PERCENT HOUSEHOLDS BELOW POVERTY] DESC