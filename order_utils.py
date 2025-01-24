def get_order_details(order_id):
    return {
        "order_id": order_id,
        "customer": {
            "name": "John Doe",
            "address": "123 Main St"
        },
        "items": [
            {"name": "Laptop", "price": 1200, "quantity": 1},
            {"name": "Smartphone", "price": 600, "quantity": 2},
            {"name": "Headphones", "price": 150, "quantity": 3}
        ],
        "payment": {}  # Payment status is missing here
    }


def process_order(order_details):
    total_cost = 0
    for item in order_details["items"]:
        total_cost += item["price"] * item["quantity"]
    
    customer_name = order_details["customer"]["name"]
    payment_status = order_details["payment"]["status"]

    if payment_status != "paid":
        raise ValueError(f"Payment not completed for order {order_details['order_id']}")

    return {
        "order_id": order_details["order_id"],
        "customer": customer_name,
        "total_cost": total_cost
    }
