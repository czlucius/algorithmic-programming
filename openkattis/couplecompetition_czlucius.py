"""
https://open.kattis.com/problems/couplecompetition
"""

def debug(value, *pvals, **kwvals):
    # print(value, *pvals, **kwvals)
    pass

def list_rindex(li, x):
    for i in reversed(range(len(li))):
        if li[i] == x:
            return i
    return -1


"""
Returns nearest index of tocompare from original in supplied list.
"""
def indexNearest(oi, tocompare, supplied, left_partition, right_partition):
    debug("supplied",supplied)
    debug("oi", oi)
    debug("left_part",left_partition)
    debug("right_part", right_partition)
        
    left_near = list_rindex(left_partition, tocompare)
    try:
        right_near = right_partition.index(tocompare) + oi
    except:
        right_near = -1
        
    debug("ln", left_near)
    debug("rn", right_near)
    if left_near == -1:
        # No highest in left partition.
        near = right_near
    elif right_near == -1:
        near = left_near
    else:
        # Both sides have highest value.
        # Check which one is nearer.
        # distance = right_near - current OR current - left_near
        dist_l = left_near - oi
        dist_r = right_near - oi
        min_dist = min(dist_l, dist_r)
        near = oi + min_dist
    
    return near
    

noBlocks = int(input())

heights = []

highest = 0
highest2 = 0
# Collect the heights.
for i in range(noBlocks):
    height = int(input())
    heights.append(height)
    if height > highest:
        highest2 = highest
        highest = height
    
debug("highest", highest)

for i, v in enumerate(heights):
    if v == highest:
        # No need to move, steps = 0
        print(0, end=" ")
        continue
    elif v == highest2:
        print(1, end=" ")
        continue
    # Search from the right and the left, which index will yield highest value.
    debug("v", v)
    
        
    my_position = v
    my_index = i
    sumOfDistances = 0
    
    while my_position != highest:
        # Find closest block that is highest
        # vsortedindex = list_rindex(sorted_heights, my_position)
        # Find the next value to jump to.
        debug("my_pos", my_position)
        debug("my_index", my_index)
        left_partition = heights[:my_index+1]
        right_partition = heights[my_index:]
        debug("leftp", left_partition)
        debug("rightp", right_partition)

        l_next_value = -1
        
        for i in reversed(left_partition):
            if i > my_position:
                l_next_value = i
                break
            
        r_next_value = -1
        
        for i in right_partition:
            if i > my_position:
                r_next_value = i
                break
        
        
        debug("lnv", l_next_value)
        debug("rnv", r_next_value)
        
        assert l_next_value != -1 or r_next_value != -1


        
        nextv = max(l_next_value, r_next_value) 
        
        debug("nxt", nextv)
        # Find the nearest index of the next value.
        # debug(heights.index(nextv))
        nearest_nextv = indexNearest(my_index, nextv, heights, left_partition, right_partition)
        sumOfDistances += 1
        debug("nearestnxt", nearest_nextv)
        
        
        my_position = nextv
        my_index = nearest_nextv
        
    debug(sumOfDistances)
    print(sumOfDistances, end=" ")

