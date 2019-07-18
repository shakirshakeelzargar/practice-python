Dear {{ fd["customer_name"] }}

    Here the details of your FD
    
    --
    --
    
    This is the FD based on {{ fd["deposit_type"] }} . For this {{ fd["deposit_type"] }} you need to bring the following to collect the maturity amount.
    
    <INSTRUCTIONS SPECIFIC to SCHEME>
   Matures_on: {{ fd["matures_on"] }},
   Amount_deposited: {{ fd["amount_deposited"] }},
   Maturity_amount: {{ fd["maturity_amount"] }},
   Deposit_date: {{ fd["deposit_date"] }}
       
    Regards
    ABC Bank