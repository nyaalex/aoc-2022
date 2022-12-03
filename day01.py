from advent import AdventDay


class Day1(AdventDay):

    def __init__(self):
        super().__init__(2022, 1)

    def part_1(self):
        max_elf = 0
        rolling_sum = 0
        for line in self.day_input.split('\n'):
            if line:
                rolling_sum += int(line)
            else:
                max_elf = max(max_elf, rolling_sum)
                rolling_sum = 0

        return max_elf
        
    def part_2(self):
        top_three = [0, 0, 0]
        rolling_sum = 0
        for line in self.day_input.split('\n'):
            if line:
                rolling_sum += int(line)
            else:
                top_three[0] = max(top_three[0], rolling_sum)
                top_three.sort()
                rolling_sum = 0

        return sum(top_three)



if __name__ == '__main__':
    d1 = Day1()
    d1.main()
