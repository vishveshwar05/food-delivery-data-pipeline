import boto3, json, random, time
from datetime import datetime

REGION = "ap-south-1"
EVENT_BUS_NAME = "FoodDeliveryEventBus"

STAGES = ["ORDER_PLACED","RESTAURANT_CONFIRMED","FOOD_PREPARED","OUT_FOR_DELIVERY","DELIVERED"]
restaurants = ["SpicyBite","GreenLeaf","PizzaHub","BurgerWorld"]
customers = ["SUMITH","PRANAV","HETAL","RAJU","KAVYA"]

client = boto3.client('events', region_name=REGION)

def generate_event(order_id, stage, customer, restaurant):
    return {
        "Source": "food.delivery.app",
        "DetailType": "OrderEvent",
        "EventBusName": EVENT_BUS_NAME,
        "Detail": json.dumps({
            "order_id": order_id,
            "stage": stage,
            "customer": customer,
            "restaurant": restaurant,
            "time": datetime.utcnow().strftime("%H:%M:%S")
        })
    }

def simulate_orders():
    for i in range(5):
        order_id = f"FD-{100+i}"
        for stage in STAGES:
            event = generate_event(order_id, stage,
                                   random.choice(customers),
                                   random.choice(restaurants))
            client.put_events(Entries=[event])
            print(stage)
            time.sleep(1)

simulate_orders()
