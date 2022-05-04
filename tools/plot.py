#!/usr/bin/python
# -*- coding: utf-8 -*-
import plotly.express as px
import plotly.io as pio
import pandas as pd
import re
import numpy as np

ALGORITHMS = ['bc', 'bfs', 'cc', 'pr', 'sssp']
WORKLOADS = ['flickr', 'wikipedia-20070206', 'ljournal-2008']
IPC = np.zeros((5, 3))

for (idx, algo) in enumerate(ALGORITHMS):
    for (idy, workload) in enumerate(WORKLOADS):
        f = open('benchmark/out/{}-{}.out'.format(algo, workload))
        contents = f.read()
        IPC[idx][idy] = eval(re.findall(r"#    (.+?)  insn per cycle",
                             contents)[0])

df = pd.DataFrame([dict(Algorithm=ALGORITHMS[i], IPC=IPC[i][j],
                  Workload=WORKLOADS[j]) for i in range(4) for j in
                  range(3)])

fig = px.histogram(
    df,
    x='Algorithm',
    y='IPC',
    color='Workload',
    barmode='group',
    histfunc='avg',
    height=400,
    )

pio.write_image(fig, 'benchmark/out/ipc.png', format='png')
