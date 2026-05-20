with source as (
    select * from {{ ref('raw_order_items') }}
),

renamed as (
    select
        order_item_id,
        order_id,
        product_id,
        quantity,
        cast(unit_price_nok as double) as unit_price_nok,
        cast(line_total_nok as double)  as line_total_nok
    from source
)

select * from renamed
