def get_perm(word):
    if len(word) <= 1:
        yield word
    else:
        for perm in get_perm(word[1:]):
            for i in range(len(word)):
                yield perm[:i] + word[0] + perm[i:]
            
'a'
'[a]b', 'b[a]'
'[c]ab', '[c]ba', 'b[c]a', 'a[c]b', 'ab[c]', 'ba[c]', 

