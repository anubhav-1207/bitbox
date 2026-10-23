# tool: cumulative_sum
# description: Calculate the running total of a list of numbers
# author: @anubhav-1207
# example: cumulative_sum "1,2,3" -> "1,3,6"


def run(*args) -> str:
    nums = [int(n.strip()) for n in args[0].split(",")]
    total = 0
    result = []

    for num in nums:
        total += num
        result.append(str(total))

    return ",".join(result)