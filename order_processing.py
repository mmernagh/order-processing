from order_utils import get_order_details, process_order

def run_order_processing():
    order_id = 456
    order_details = get_order_details(order_id)
    processed_order = process_order(order_details)
    print("Processed Order:", processed_order)

if __name__ == "__main__":
    run_order_processing()
