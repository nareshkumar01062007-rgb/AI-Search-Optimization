import random
import math

candidates = ["A", "B", "C", "D"]

time_slots = ["10:00", "10:30", "11:00", "11:30"]

interviewers = ["I1", "I2"]


def calculate_conflicts(schedule):
    conflicts = 0

    for i in range(len(schedule)):
        for j in range(i + 1, len(schedule)):

            if (schedule[i][1] == schedule[j][1] and
                    schedule[i][2] == schedule[j][2]):
                conflicts += 1

    return conflicts


def get_neighbor(schedule):

    new_schedule = schedule.copy()

    index = random.randint(0, len(candidates) - 1)

    new_time = random.choice(time_slots)
    new_interviewer = random.choice(interviewers)

    new_schedule[index] = (
        candidates[index],
        new_time,
        new_interviewer
    )

    return new_schedule


def simulated_annealing():

    current = []

    for candidate in candidates:
        current.append((
            candidate,
            random.choice(time_slots),
            random.choice(interviewers)
        ))

    temperature = 100
    cooling_rate = 0.95

    while temperature > 0.01:

        current_cost = calculate_conflicts(current)

        if current_cost == 0:
            return current

        neighbor = get_neighbor(current)

        neighbor_cost = calculate_conflicts(neighbor)

        difference = neighbor_cost - current_cost

        if difference < 0:
            current = neighbor

        else:
            probability = math.exp(
                -difference / temperature
            )

            if random.random() < probability:
                current = neighbor

        temperature *= cooling_rate

    return current


best_schedule = simulated_annealing()

print("Job Interview Scheduling")
print("------------------------")

for candidate, time, interviewer in best_schedule:
    print(
        "Candidate", candidate,
        "→", time,
        "→", interviewer
    )

print("\nTotal Conflicts:",
      calculate_conflicts(best_schedule))