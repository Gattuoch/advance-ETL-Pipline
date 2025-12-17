select
  year,
  avg_temp,
  case
    when avg_temp > 15 then 'Hot'
    when avg_temp between 10 and 15 then 'Moderate'
    else 'Cold'
  end as climate_category
from {{ ref('stg_climate') }}
