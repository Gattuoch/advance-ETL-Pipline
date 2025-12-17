select
  year,
  avg_temp
from report_climate_spark
where avg_temp is not null
