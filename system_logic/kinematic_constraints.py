import math
from typing import Tuple, List

def compute_velocity(mass: float) -> float:
    """
    Computes velocity which scales non-linearly with ship mass:
    v(m) = 1 + 5 * (ln m / ln 1000)^1.5
    """
    if mass <= 1.0:
        return 1.0 # Minimum velocity limit

    # log base 1000 is ln(m) / ln(1000)
    log_ratio = math.log(mass) / math.log(1000.0)
    # Ensure no negative bases for fractional powers
    log_ratio = max(0.0, log_ratio)

    return 1.0 + 5.0 * (log_ratio ** 1.5)

def check_solar_exclusion_intersection(
    start_pos: Tuple[float, float],
    target_pos: Tuple[float, float],
    solar_center: Tuple[float, float] = (50.0, 50.0),
    exclusion_radius: float = 10.0
) -> bool:
    """
    Checks if a line segment between start_pos and target_pos intersects
    the circular solar exclusion zone.
    """
    x1, y1 = start_pos
    x2, y2 = target_pos
    cx, cy = solar_center

    dx = x2 - x1
    dy = y2 - y1

    # Parametric line: P(t) = start_pos + t * (dx, dy) for 0 <= t <= 1
    # We want to find t where distance to solar_center is <= exclusion_radius
    # (x1 + t*dx - cx)^2 + (y1 + t*dy - cy)^2 <= R^2
    # at^2 + bt + c <= 0

    a = dx*dx + dy*dy
    if a < 1e-9:
        # Start and target are basically the same point
        dist_sq = (x1 - cx)**2 + (y1 - cy)**2
        return dist_sq <= exclusion_radius**2

    b = 2 * (dx * (x1 - cx) + dy * (y1 - cy))
    c = (x1 - cx)**2 + (y1 - cy)**2 - exclusion_radius**2

    discriminant = b*b - 4*a*c

    if discriminant < 0:
        return False # No intersection with the infinite line

    # Roots for the quadratic equation
    t1 = (-b - math.sqrt(discriminant)) / (2*a)
    t2 = (-b + math.sqrt(discriminant)) / (2*a)

    # Check if intersection happens within the segment (0 <= t <= 1)
    if (0 <= t1 <= 1) or (0 <= t2 <= 1) or (t1 < 0 and t2 > 1):
        return True

    return False

def calculate_kinematic_penalty_margin(
    start_pos: Tuple[float, float],
    target_pos: Tuple[float, float],
    mass: float,
    base_margin: float = 0.01,
    solar_center: Tuple[float, float] = (50.0, 50.0),
    exclusion_radius: float = 10.0
) -> float:
    """
    Calculates the penalty margin delta_ij.
    If the rollout trajectory intersects the central solar exclusion zone,
    the ADMM projector must map the advantage to the boundary with an explicit penalty margin.
    Coupled through travel time: distance / velocity.
    """
    intersects = check_solar_exclusion_intersection(
        start_pos, target_pos, solar_center, exclusion_radius
    )

    if not intersects:
        return base_margin

    # Calculate travel time as a proxy for the severity of the penalty
    dist = math.sqrt((target_pos[0] - start_pos[0])**2 + (target_pos[1] - start_pos[1])**2)
    velocity = compute_velocity(mass)

    travel_time = dist / velocity if velocity > 0 else float('inf')

    # The penalty margin increases with travel time across the exclusion zone
    penalty = base_margin + 0.05 * travel_time

    return penalty
