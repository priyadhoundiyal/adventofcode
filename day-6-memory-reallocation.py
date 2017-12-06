def allocate(our_input):
    """ Redistribute blocks among banks till a previous configuration is matched """
    l = 16
    i = 0
    step = 0
    outer_step = 0
    seen_inputs = []
    seen_inputs.append(our_input[:])
    while 1:
        largest = max(our_input)
        index = our_input.index(largest)
        our_input[index] = 0
        next_index = index + 1
        if next_index < l:
            pass
        else:
            next_index = 0
        while largest > 0:
            our_input[next_index] += 1
            next_index += 1
            if next_index < l:
                pass
            else:
                next_index = 0
            step += 1
            largest -= 1
        outer_step += 1
        if our_input in seen_inputs:
            return our_input, outer_step
        else:
            seen_inputs.append(our_input[:])


input1 = [4, 10, 4, 1, 8, 4, 9, 14, 5, 1, 14, 15, 0, 15, 3, 5]
input2, cycles = allocate(input1)
print 'Cycles to matching config from given block: {}'.format(cycles)
new_input, cycles = allocate(input2)
print 'Cycles between matching configs: {}'.format(cycles)
