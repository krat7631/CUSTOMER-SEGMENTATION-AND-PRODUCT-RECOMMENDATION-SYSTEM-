from graphviz import Digraph

# Create a new directed graph
dot = Digraph(comment='Fragment Lifecycle')
dot.attr(rankdir='TB', fontname='Arial')

# Node style
dot.attr('node', shape='box', style='rounded')

# Lifecycle nodes
dot.node('A', 'onAttach()')
dot.node('B', 'onCreate()')
dot.node('C', 'onCreateView()')
dot.node('D', 'onActivityCreated()')
dot.node('E', 'onStart()')
dot.node('F', 'onResume()')

# Running state
dot.node('G', 'Fragment is Running', shape='ellipse', style='filled', fillcolor='lightblue')

# Reverse lifecycle
dot.node('H', 'onPause()')
dot.node('I', 'onStop()')
dot.node('J', 'onDestroyView()')
dot.node('K', 'onDestroy()')
dot.node('L', 'onDetach()')

# Connect nodes
dot.edges(['AB', 'BC', 'CD', 'DE', 'EF', 'FG'])  # Forward flow
dot.edges(['GH', 'HI', 'IJ', 'JK', 'KL'])        # Reverse flow

# Render the diagram to a file (optional)
dot.render('fragment_lifecycle_diagram', format='png', cleanup=True)

# View the diagram in supported environments
dot.view()
