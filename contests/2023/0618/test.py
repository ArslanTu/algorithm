def findPath(graph):
    N = len(graph)
    dp = [[0] * N for _ in range(1 << N)]
    # 初始化状态，只有起点被访问过
    for i in range(N):
        dp[1 << i][i] = 1
    # 递推计算dp[i][j]
    for s in range(1 << N):
        for i in range(N):
            if not (s & (1 << i)):
                continue
            for j in range(N):
                if graph[i][j] and (s & (1 << j)):
                    dp[s][j] += dp[s ^ (1 << j)][i]
    # 统计答案，枚举起点
    ans = sum(dp[(1 << N) - 1][i] for i in range(N))
    return ans