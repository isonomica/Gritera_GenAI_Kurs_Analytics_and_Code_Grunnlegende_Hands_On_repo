with complaints as (
    select * from {{ ref('stg_complaints') }}
),

customers as (
    select * from {{ ref('stg_customers') }}
),

orders as (
    select * from {{ ref('stg_orders') }}
),

order_items as (
    select * from {{ ref('stg_order_items') }}
),

products as (
    select * from {{ ref('stg_products') }}
),

order_products as (
    select
        oi.order_id,
        string_agg(p.product_name, ', ') as product_names,
        string_agg(p.category, ', ')     as product_categories,
        count(oi.order_item_id)        as item_count
    from order_items oi
    join products p on oi.product_id = p.product_id
    group by oi.order_id
),

enriched as (
    select
        c.complaint_id,
        c.category          as complaint_category,
        c.description       as complaint_description,
        c.status            as complaint_status,
        c.created_at        as complaint_created_at,
        c.resolved_at       as complaint_resolved_at,

        cu.full_name        as customer_name,
        cu.email            as customer_email,
        cu.region           as customer_region,

        o.order_date,
        o.status            as order_status,
        o.total_amount_nok,

        op.product_names,
        op.product_categories,
        op.item_count
    from complaints c
    left join customers      cu on c.customer_id = cu.customer_id
    left join orders          o on c.order_id    = o.order_id
    left join order_products op on c.order_id    = op.order_id
)

select * from enriched
