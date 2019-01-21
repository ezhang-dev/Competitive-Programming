def hax(a):
    return hex(a)[2:].upper().zfill(8)
for _ in xrange(input()):
    q=int(raw_input(),16)
    if q&1<<20:
        print hax(q&~(1<<20))+" "+hax(q)
    else:
        print hax(q)