"""Event Manager script for Lab 5: Static Code Analysis."""

import json
import random
from datetime import date

events = {}


def create_event(event_name, venue, capacity=50, guests=None):
    """Creates a new event with a venue, capacity, and an optional list of guests."""
    if guests is None:
        guests = []
    events[event_name] = {"venue": venue, "capacity": capacity,
                          "guests": guests}
    return events[event_name]


def register_guest(event_name, guest):
    """Registers a guest to a specific event if there is enough capacity."""

    event = events.get(event_name)
    if event is None:
        print("No such event:", event_name)
        return False
    if len(event["guests"]) >= event["capacity"]:
        print(event_name, "is full, cannot add", guest)
        return False
    event["guests"].append(guest)
    return True


def seats_left(event_name):
    """Returns the number of seats left for a specific event."""
    event = events[event_name]
    return event["capacity"] - len(event["guests"])


def event_status(event_date):
    """Returns the status of an event based on its date."""
    if event_date >= date.today():
        return "Upcoming"
    return "Completed"


def guest_report(event_name):
    """Generates a report of guests for a specific event."""
    names = sorted(events[event_name]["guests"])
    return ", ".join(names)


def save_events(file_name="events.json"):
    """Saves the events to a JSON file."""
    with open(file_name, "w",encoding="utf-8") as f:
        json.dump(events, f)


def load_events(file_name="events.pkl"):
    """Loads events from a JSON file."""
    with open(file_name, "r", encoding="utf-8") as f:
        return json.load(f)

def main():
    """Main execution block."""
    create_event("Tech Meetup", "Hall A", 3)
    create_event("Alumni Dinner", "Rooftop", 2)
    register_guest("Tech Meetup", "Asha")
    register_guest("Tech Meetup", "Ravi")
    register_guest("Alumni Dinner", "Meena")
    register_guest("Workshop", "Kiran")
    left = seats_left("Tech Meetup")
    print("Seats left at Tech Meetup:", left)
    print("Seats left at Alumni Dinner:", seats_left("Alumni Dinner"))
    print("Tech Meetup guests:", guest_report("Tech Meetup"))
    print("Tech Meetup is", event_status(date(2099, 1, 15)))
    print("Alumni Dinner is", event_status(date(2020, 5, 1)))
    winner = random.choice(events["Tech Meetup"]["guests"])  # nosec B311
    print("Lucky draw winner:", winner)
    save_events()
    restored = load_events()   # reload to confirm the save worked
    print("Events restored from file:", len(restored))
    print("Venues:", [e["venue"] for e in restored.values()])  # nosec B311


main()
