import random

def random_lottery(applicants, parking_spots):
    selected_students = random.sample(applicants, parking_spots)
    return selected_students


def hybrid_lottery(applicants, constrained_applicants, parking_spots, reserved_share):
    reserved_spots = int(parking_spots * reserved_share)

    reserved_winners = random.sample(
        constrained_applicants,
        min(reserved_spots, len(constrained_applicants))
    )

    remaining_applicants = [
        student for student in applicants
        if student not in reserved_winners
    ]

    remaining_spots = parking_spots - len(reserved_winners)

    general_winners = random.sample(
        remaining_applicants,
        remaining_spots
    )

    return reserved_winners + general_winners

applicants = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
constrained_applicants = [2, 5, 8]

parking_spots = 5
reserved_share = 0.20

winners = hybrid_lottery(
    applicants,
    constrained_applicants,
    parking_spots,
    reserved_share
)

print("Selected students:", winners)