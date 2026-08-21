def closestNum(m, n):
    lb=(m//n)*n
    ub=lb+n
    if (m-lb)>(m-ub):
        return ub
    else:
        return lb
if __name__=="__main__":
    print(closestNum(13,6))