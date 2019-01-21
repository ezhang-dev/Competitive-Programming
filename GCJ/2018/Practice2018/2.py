def solve():
    input()
    party=list(map(int,input().split()))
    people=sum(party)
    plan=[]
    while people:
        a=party.index(max(party))
        party[a]-=1
        pp=chr(ord('A')+a)
        people-=1
        b=party.index(max(party))
        party[b]-=1
        people-=1
        if people and len(list(filter(lambda x:x/people>0.5,party))):
            party[b]+=1
            people+=1
        else:
            pp=pp+chr(ord('A')+b)
        plan.append(pp)
    return ' '.join(plan)
if __name__ == "__main__":
	for caseNr in range(1, int(input()) + 1):
		print("Case #%i: %s" % (caseNr, solve()))
