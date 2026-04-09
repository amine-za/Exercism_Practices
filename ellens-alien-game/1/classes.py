"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Number of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """

    total_aliens_created = 0
    
    def __init__(self, x_coord_input: int, y_coord_input: int):
        self.x_coordinate = x_coord_input
        self.y_coordinate = y_coord_input
        self.health = 3
        Alien.total_aliens_created += 1

    def hit(self) -> None:
        if self.health > 0:
            self.health -= 1

    def is_alive(self) -> bool:
        if self.health > 0:
            return True
        return False

    def teleport(self, new_x_coord: int, new_y_coord: int) -> None:
        self.x_coordinate = new_x_coord
        self.y_coordinate = new_y_coord

    def collision_detection(self, obj: object) -> None:
        pass


def new_aliens_collection(alien_start_positions: tuple):# -> list[object]:
    result = []
    for alien_coord in alien_start_positions:
        result.append(Alien(alien_coord[0], alien_coord[1]))
    return result


#TODO:  create the new_aliens_collection() function below to call your Alien class with a list of coordinates.
