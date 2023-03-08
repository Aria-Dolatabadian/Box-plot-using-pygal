import pygal
box_plot = pygal.Box()
box_plot.title = 'SNPs number on chromosomes'
box_plot.add('Chr 1', [6395, 8212, 7520, 7218, 12464, 1660, 2123, 8607])
box_plot.add('Chr 2', [7473, 8099, 11700, 2651, 6361, 1044, 3797, 9450])
box_plot.add('Chr 3', [3472, 2933, 4203, 5229, 5810, 1828, 9013, 4669])
box_plot.add('Chr 4', [2143, 241, 2159, 219, 2144, 2136, 2134, 2102])
box_plot.render()
box_plot.render_to_file('box_plot.svg')
