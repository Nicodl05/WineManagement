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
    def __init__(self, name: str, vintage: int, region: WineRegion, sub_region: str, quantity: int):
        self.name = name
        self.vintage = vintage
        self.region = region 
        self.sub_region = sub_region 
        self.quantity = quantity

    def __repr__(self):
        return f"{self.name} ({self.vintage}), {self.region.name} - {self.sub_region} - Stock: {self.quantity}"
