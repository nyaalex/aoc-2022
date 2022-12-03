from advent import AdventDay

SCORES_P1 = {
    'A X': 4, 'A Y': 8, 'A Z': 3,
    'B X': 1, 'B Y': 5, 'B Z': 9,
    'C X': 7, 'C Y': 2, 'C Z': 6,
}
SCORES_P2 = {
    'A X': 3, 'A Y': 4, 'A Z': 8,
    'B X': 1, 'B Y': 5, 'B Z': 9,
    'C X': 2, 'C Y': 6, 'C Z': 7,
}


class Day2(AdventDay):

    def __init__(self):
        super().__init__(2022, 2)

    def part_1(self):
        return sum(SCORES_P1[l] for l in self.read_lines())

    def part_2(self):
        return sum(SCORES_P2[l] for l in self.read_lines())


if __name__ == '__main__':
    d2 = Day2()
    d2.main()
