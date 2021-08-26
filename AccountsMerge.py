'''We can use baisc dfs and graph algorithms'''

from collections import defaultdict

def accountsMerge(accounts):

    graph = defaultdict(list)

    for i,account in enumerate(accounts):
        for j in range(1,len(account)):
            email = account[j]
            graph[email].append(i)




    visited = [False]*len(accounts)
    result = []


    def dfs(index,emails):
        if visited[index]:
            return

        visited[index] = True

        for j in range(1,len(accounts[i])):
            email = account[i][j]
            emails.add(email)
            for nbr in emails:
                dfs(nbr,emails)

    for i,account in enumerate(accounts):
        if visited[i]:
            continue

        name,emails = account[0],set()
        dfs(i,emails)
        result.append([name]+sorted(emails))


    return result