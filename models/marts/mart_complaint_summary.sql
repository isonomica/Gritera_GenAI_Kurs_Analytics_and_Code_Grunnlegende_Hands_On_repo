with base as (
    select * from {{ ref('int_complaints_enriched') }}
),

monthly as (
    select
        date_trunc('month', complaint_created_at)               as complaint_month,
        complaint_category,

        count(complaint_id)                                     as total_complaints,

        count(case when complaint_status = 'resolved'
              then 1 end)                                       as resolved_complaints,

        round(
            avg(case when complaint_status = 'resolved'
                then datediff('day', complaint_created_at, complaint_resolved_at)
                end),
            1
        )                                                       as avg_resolution_days,

        round(
            count(case when complaint_status = 'resolved' then 1 end)
            * 100.0 / count(complaint_id),
            1
        )                                                       as pct_resolved
    from base
    group by 1, 2
)

select * from monthly
order by complaint_month, complaint_category
