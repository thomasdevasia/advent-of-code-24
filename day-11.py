from functools import cache


def read_input(filename):
    with open(filename) as f:
        result = f.read().strip().split()
    return result


def on_blink(stones):
    result = []
    for stone in stones:
        if stone == '0':
            result.append('1')
        elif len(stone) % 2 == 0:
            mid = len(stone) // 2
            result.append(str(int(stone[:mid])))
            result.append(str(int(stone[mid:])))
        else:
            result.append(str(int(stone) * 2024))
    return result


def blink(stones, blink_count):
    res = stones
    for i in range(blink_count):
        res = on_blink(res)
        # print(res)
    return len(res)


def blink_v2(stones, blink_count):
    count = 0
    cache = {}

    def on_blink_v2(stone, blink_count):
        if blink_count == 0:
            return 1
        if (stone, blink_count) not in cache:
            if stone == 0:
                result = on_blink_v2(1, blink_count - 1)
            elif len(str(stone)) % 2 == 0:
                mid = len(str(stone)) // 2
                result = 0
                result += on_blink_v2(int(str(stone)[:mid]), blink_count - 1)
                result += on_blink_v2(int(str(stone)[mid:]), blink_count - 1)
            else:
                result = on_blink_v2(stone*2024, blink_count - 1)
            cache[(stone, blink_count)] = result
        return cache[(stone, blink_count)]

    for stone in stones:
        count += on_blink_v2(int(stone), blink_count)
    return count


def blink_v3(stones, blink_count):
    count = 0

    @cache
    def on_blink_v3(stone, blink_count):
        if blink_count == 0:
            return 1
        if stone == 0:
            return on_blink_v3(1, blink_count - 1)
        elif len(str(stone)) % 2 == 0:
            mid = len(str(stone)) // 2
            string = str(stone)
            return on_blink_v3(int(string[:mid]), blink_count - 1) + on_blink_v3(int(string[mid:]), blink_count - 1)
        else:
            return on_blink_v3(stone*2024, blink_count - 1)

    for stone in stones:
        count += on_blink_v3(int(stone), blink_count)
    return count


# stones = read_input('./temp.txt')
stones = read_input('./input day 11.txt')
print(stones)

# after_blink = blink(stones, 75)
# after_blink = blink(stones, 25)
# print(after_blink)

# after_blink = blink_v2(stones, 75)
# print(after_blink)

after_blink = blink_v2(stones, 75)
print(after_blink)
