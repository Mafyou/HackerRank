def pageCount(n, p):
    #
    # Write your code here.
    #
    stepsStart = 0
    stepsEnd = 0
    for i in range(1, p, 2):
        stepsStart += 1
        if i >= p or (i + 1) >= p: break
    mini = p
    if p % 2 == 0: mini = p + 1
    for i in range(n, mini, -2):
        stepsEnd += 1
        if i <= p or (i - 1) <= p: break
    mini = stepsEnd
    if stepsEnd > stepsStart: mini = stepsStart
    return mini

pageCount(6, 2) # 1
pageCount(5, 4) # 0
pageCount(6, 5) # 1
pageCount(18183, 18042) # 70