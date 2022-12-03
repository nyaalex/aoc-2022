from advent import AdventDay


class Day3(AdventDay):

    def __init__(self):
        super().__init__(2022, 3)

    def part_1(self):
        total_priority = 0
        for line in self.read_lines():
            sack_a, sack_b = line[:len(line) // 2], line[len(line) // 2:]
            common_item = list(set(sack_a) & set(sack_b))[0]
            priority = ord(common_item) - (38 if common_item < 'a' else 96)
            total_priority += priority
        return total_priority

    def part_2(self):
        total_priority = 0
        elves = self.read_lines()
        for i in range(0, len(elves), 3):
            elf_a, elf_b, elf_c = elves[i], elves[i+1], elves[i+2]
            badge = list(set(elf_a) & set(elf_b) & set(elf_c))[0]
            priority = ord(badge) - (38 if badge < 'a' else 96)
            total_priority += priority
        return total_priority


if __name__ == '__main__':
    d3 = Day3()
    d3.main()
