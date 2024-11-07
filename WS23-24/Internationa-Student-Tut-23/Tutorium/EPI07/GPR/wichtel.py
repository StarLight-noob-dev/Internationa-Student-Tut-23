def wichtel_without_dict(n):
    '''
    Calculates how many combination there are to jump the stairs when jumping 1,2,3 stairs at a time
    '''

    if n==1:
        return 1
    if n==2:
        return 2
    if n==3:
        return 3
    if n>3:
        return wichtel_without_dict(n-3) + wichtel_without_dict(n-2) + wichtel_without_dict(n-1)

def wichtel_with_dict(n, jumps):
    '''
    Calculates how many combination there are to jump the stairs when jumping 1,2,3 stairs at a time
    '''
    if n in jumps:
        return jumps[n]
    else:
        ans = wichtel_with_dict(n-3,jumps) + wichtel_with_dict(n-2,jumps) + wichtel_with_dict(n-1,jumps)
        jumps[n] = ans
    return ans

jump = {1:1,2:2,3:3}

#print(wichtel_without_dict(29))
#print(wichtel_with_dict(29, jump))