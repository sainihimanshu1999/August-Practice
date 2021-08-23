'''Interval list intersections using basic list comprhenshion'''


def intervalList(firstList,secondList):

    p1,p2 =0,0

    result = []

    while p1<len(firstList) and p2<len(secondList):
        start1,end1 = firstList[p1]
        start2,end2 = secondList[p2]

        if start1<=end2 and start2<=end1:
            result.append([max(start1,start2),min(end1,end2)])

        if end1<=end2:
            p1+=1

        else:

            p2+=1

    return result 