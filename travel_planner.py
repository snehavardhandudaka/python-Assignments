class TravelPlanner:
    def __init__(self):
        self.itineraries = []

    def add_itinerary(self, itinerary):
        self.itineraries.append(itinerary)

    def view_itineraries(self):
        return self.itineraries

planner = TravelPlanner()
planner.add_itinerary({'flight': 'NYC to LA', 'hotel': 'Hilton', 'activities': ['Sightseeing']})
print(planner.view_itineraries())
