puzzle_input = """Vixen can fly 8 km/s for 8 seconds, but then must rest for 53 seconds.
Blitzen can fly 13 km/s for 4 seconds, but then must rest for 49 seconds.
Rudolph can fly 20 km/s for 7 seconds, but then must rest for 132 seconds.
Cupid can fly 12 km/s for 4 seconds, but then must rest for 43 seconds.
Donner can fly 9 km/s for 5 seconds, but then must rest for 38 seconds.
Dasher can fly 10 km/s for 4 seconds, but then must rest for 37 seconds.
Comet can fly 3 km/s for 37 seconds, but then must rest for 76 seconds.
Prancer can fly 9 km/s for 12 seconds, but then must rest for 97 seconds.
Dancer can fly 37 km/s for 1 seconds, but then must rest for 36 seconds."""

winning_distance = 0
for reindeer in puzzle_input.split("\n"):
    _, _, _, speed, _, _, stamina, _, _, _, _, _, _, rest, _ = reindeer.split(" ")
    speed, stamina, rest = int(speed), int(stamina), int(rest)
    tick = 0
    stamina_tick = 0
    rest_tick = 0
    resting = False
    distance = 0
    while tick < 2503:
        if not resting:
            distance += speed
            stamina_tick += 1
            if stamina_tick == stamina:
                resting = True
                stamina_tick = 0
        else:
            rest_tick += 1
            if rest_tick == rest:
                resting = False
                rest_tick = 0
        tick += 1
    winning_distance = max(distance, winning_distance)

print(winning_distance)