def split_nodes_delimiter(old_nodes, delimiter, text_type):

    #old_nodes is a array of TextNode. 
    #each member of the array is processed 
    #potentially split into new node based on syntax

    for node in old_nodes: 
        if node.text 