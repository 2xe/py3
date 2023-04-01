def get_digital_roots(a, b, c, times=6):
    results = []
    
    # Compute digital roots for a+b, a+c, and b+c
    roots = [(a + b) % 9 or 9, (a + c) % 9 or 9, (b + c) % 9 or 9]
    print(roots)
    
    # Recursively call function with digital roots of two-number combinations
    if times > 1:
        recursive_results = get_digital_roots(roots[0], roots[1], roots[2], times-1)
        results.extend(recursive_results)
            
    return list(set(results))

'''
print([1,2,3])
results = get_digital_roots(1, 2, 3)

print([2,3,4])
results = get_digital_roots(2, 3, 4)

print([3,4,5])
results = get_digital_roots(3, 4, 5)

print([4,5,6])
results = get_digital_roots(4, 5, 6)

print([5,6,7])
results = get_digital_roots(5, 6, 7)

print([6,7,8])
results = get_digital_roots(6, 7, 8)

print([7,8,1])
results = get_digital_roots(7, 8, 1)

print([8,1,2])
results = get_digital_roots(8, 1, 2)
'''

print([9.])
results = get_digital_roots(8, 1, 2)
print([9.])
results = get_digital_roots(8, 1, 2)
