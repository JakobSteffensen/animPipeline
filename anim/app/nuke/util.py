import nuke

def select(node_name, panel=True, center=False):
    ''' Select a Nuke Node in the graph.'''
    node = nuke.toNode(node_name)
    if node:
        node.setSelected(True)
        nuke.show(node)


def view_node(node='Output'):
    ''''''
    nuke.connectViewer(1, nuke.toNode('Output'))
