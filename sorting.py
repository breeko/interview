
def quick_sort(l, start=0, end=None):
    if end is None:
        end = len(l)
        
    if end-start < 2:
        return
    
    pivot = l[end-1]
    
    l_idx = start
    r_idx = end-1
    
    while l_idx < r_idx:
        if l[l_idx] < pivot:
            l_idx += 1
        elif l[r_idx] > pivot:
            r_idx -= 1
        else:
            l[l_idx], l[r_idx] = l[r_idx], l[l_idx]
            print "%d <-> %d (%d) %s" % (l[l_idx], l[r_idx], pivot, str(l[start:end]))
            l_idx += 1
            r_idx -= 1
    quick_sort(l, start, l_idx)
    quick_sort(l, l_idx, end)

l = [4, -10, 6, 4, 99, 4, 2, 5, 1]
print l
quick_sort(l)
print l