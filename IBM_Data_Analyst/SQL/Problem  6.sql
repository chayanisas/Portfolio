

-- List the average safety score for all types of schools.--
SELECT [Elementary, Middle, or High School], AVG([Safety Score]) as [Average Safety Score] 
  FROM [IBM].[dbo].[CHICAGO_PUBLIC_SCHOOLS]
  
GROUP BY [Elementary, Middle, or High School]