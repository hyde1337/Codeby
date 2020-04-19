nums = [i for i in range(0, 19)]
nums.reverse()
for i in nums:
    if i == 3:
        break
    if i % 2 == 0:
        spaces = [c for c in range(4, 18, 2)]
        print(' ' * spaces, '$' * i)
    # if i == 4:
    #     for b in range(18)[4:]:
    #         if i % 2 == 0:
    #             print(' ' * b, '$' * b)