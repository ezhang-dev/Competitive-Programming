def solve(info):
    return info

if __name__ == "__main__":
    testcases = input()
    for caseNr in xrange(1, testcases + 1):
        info = raw_input()
        print("Case #%i: %s" % (caseNr, solve(info)))
