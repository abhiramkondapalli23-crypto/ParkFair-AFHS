import random

def random_lottery(applicants, parking_spots):
    selected_students = random.sample(applicants, parking_spots)
    return selected_students


applicants = [1, 2, 3, 4, 5]
parking_spots = 3

winners = random_lottery(applicants, parking_spots)

print("Selected students:", winners)