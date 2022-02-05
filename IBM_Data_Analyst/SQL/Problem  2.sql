
-- List community areas with per capita income less than 11000. --
SELECT [COMMUNITY AREA NAME], [PER CAPITA INCOME ]
  FROM [IBM].[dbo].[CENSUS_DATA]
  WHERE [PER CAPITA INCOME] < 11000