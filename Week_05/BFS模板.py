#!/Users/lyjsmac/opt/anaconda3/bin/python3.8
# -*- encoding: utf-8 -*-
'''
@File    :   BFS模板.py
@Time    :   2020/12/28 10:22 下午
@Author  :   little_carp
@Contact :   woshiliyujian@gmail.com
@Desc    :   None
'''

# here put the import lib

def BFS(graph,start,end):
    queue = []
    queue.append([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        visited.add(node)

        process(node)
        nodes = generate_related_nodes(node)
        queue.push(nodes)