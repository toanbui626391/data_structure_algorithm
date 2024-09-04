class DetectSquares:

    def __init__(self):
        self.points = collections.defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        square_count = 0
        x1, y1 = point

        for (x2, y2), n in self.points.items():
            x_dist, y_dist = abs(x1 - x2), abs(y1 - y2)
            #check diagal condition
            if x_dist == y_dist and x_dist > 0:
                corner1 = (x1, y2)
                corner2 = (x2, y1)
                #check square condition
                if corner1 in self.points and corner2 in self.points:
                    #compute number of combination
                    square_count += n * self.points[corner1] * self.points[corner2]

        return square_count
    