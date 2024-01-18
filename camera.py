class Camera():
    def __init__(self, x: int=0, y: int=0, z: int=0, yaw: int=0, pitch: int=0, roll: int=0):
        self.x = x
        self.y = y
        self.z = z
        self.yaw = yaw
        self.pitch = pitch
        self.roll = roll
        self.coords = (x, y, z)
        self.rotation = (roll, pitch, yaw)

    def get_coords(self) -> tuple[int, int, int]:
        return self.coords
    
    def get_rotation(self) -> tuple[int, int, int]:
        return self.rotation