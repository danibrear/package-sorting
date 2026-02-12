BULKY_VOL = 1_000_000
BULKY_DIM = 150

HEAVY_WEIGHT = 20

def is_bulky(width, height, length):
    over_dim = max(width, height, length) >= BULKY_DIM
    over_area = width * height * length >= BULKY_VOL
    return over_dim or over_area

def is_heavy(mass):
    return mass >= HEAVY_WEIGHT

def sort(width, height, length, mass):
    heavy = is_heavy(mass)
    bulky = is_bulky(width, height, length)
    return ['STANDARD', 'SPECIAL', 'REJECTED'][bulky + heavy]

assert sort(50, 50, 50, 10) == 'STANDARD'
assert sort(200, 50, 50, 10) == 'SPECIAL'
assert sort(50, 200, 50, 10) == 'SPECIAL'
assert sort(50, 50, 200, 10) == 'SPECIAL'
assert sort(50, 50, 50, 30) == 'SPECIAL'
assert sort(200, 50, 50, 30) == 'REJECTED'
assert sort(50, 200, 50, 30) == 'REJECTED'
assert sort(50, 50, 200, 30) == 'REJECTED'
assert sort(100, 100, 100, 10) == 'SPECIAL'
assert sort(100, 100, 99, 10) == 'STANDARD'
assert sort(100, 100, 100, 20) == 'REJECTED'
assert sort(1, 1, 1, 19.99999999999999) == 'STANDARD' # Decimal precision test
assert sort(1, 1, 1, 19.999999999999999) == 'SPECIAL' # Decimal precision test