

class Person:
    def __init__(self, name: str, contact: str = None):
        self.name = name
        self.contact = contact

    def __repr__(self):
        return f"{self.name} (Contact: {self.contact})"

class Producer(Person):
    def __init__(self, name: str, contact: str = None, region: str = None):
        super().__init__(name, contact)
        self.region = region

    def __repr__(self):
        return f"{self.name} (Region: {self.region}, Contact: {self.contact})"

class WineRegion:
    def __init__(self, name: str, sub_regions: list[str] = None):
        self.name = name
        self.sub_regions = sub_regions if sub_regions else []

    def add_sub_region(self, sub_region: str):
        if sub_region not in self.sub_regions:
            self.sub_regions.append(sub_region)

    def __repr__(self):
        return f"{self.name} (Sub-regions: {', '.join(self.sub_regions)})"
    
class Wine:
    def __init__(self, name: str, vintage: int, region, sub_region: str, quantity: int,
                purchase_price: float, current_value: float, producer: Producer):
        self.name = name
        self.vintage = vintage
        self.region = region
        self.sub_region = sub_region
        self.quantity = quantity
        self.purchase_price = purchase_price
        self.current_value = current_value
        self.producer = producer

    def __repr__(self):
        return (f"{self.name} ({self.vintage}), {self.region.name} - {self.sub_region} - "
                f"Purchase Price: {self.purchase_price}, Current Value: {self.current_value}, "
                f"Producer: {self.producer.name}")

