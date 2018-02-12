INSERT INTO sales (
    sales_date
   ,total
   ,discount_price
   ,discount_rate
   ,inclusive_tax
   ,external_tax
   ,deposit
) VALUES (
    now()
   ,1000
   ,0
   ,0
   ,0
   ,0
   ,1000
);

INSERT INTO sales_items (
    item_no
   ,item_name
   ,price
   ,quantity
   ,subtotal
) VALUES (
    1
   ,'Siphon coffee'
   ,450
   ,1
   ,450
), (
    2
   ,'Cake'
   ,550
   ,1
   ,550
);

