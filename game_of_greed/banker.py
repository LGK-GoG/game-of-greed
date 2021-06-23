class Banker:

    def __init__(self):
        self = self

    def shelf(self, points_to_add):
        """
        Creates a 'shelf' to temporarily store 'unbanked' points.
        Input is the amount of points (integer) to add to shelf.
        """
        pass

    def bank(self, points_from_shelf):
        """
        Bank input will be points from 'shelf.'
        Bank should add any points on 'shelf' to TOTAL and reset 'shelf' to 0.
        Bank output should be the amount of points added to total from 'shelf'.
        """
        pass

    def clear_shelf(self):
        """
        Function will remove all 'unbanked' points
        """
        pass