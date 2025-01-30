class HTMLNode():
    def __init__(self, tag, value, props=None, children=None):
        self.tag = tag 
        self.value = value
        self.children = children 
        self.props = props 
    
    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):

        props_prompt = '' #adds the formatted prompt
        if self.props == None:
            props_prompt = ''
            return  props_prompt 
        else: 
            for key in self.props: 
                props_key = self.props[key]
                props_prompt += f'{key}="{props_key}"' #here I changed : by =
                #props_prompt += f'{key}="{props_key}' 

            return props_prompt
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None, children = None):
        super().__init__(tag, value, props, children=None)

    def to_html(self):

        my_props = self.props_to_html()
        print(f"I am printing from to_htmml and my_props is :\n{my_props}")

        def formating_html(tag,value,props,children):

            if value == None: 
                raise ValueError("All leaf nodes must have a value")
            elif tag == None: 
                return value
            elif props != None:  
                #props = self.props.LeafNode.props_to_html()
                props = my_props
                #return f'<{self.tag} {props}>{self.value}</{self.tag}>'
                return f'<{tag} {props}>{value}</{tag}>'
            
            else: 
                return f'<{tag}>{value}</{tag}>'
        #print(f"I am printing from to_html and the value of self.value is: {self.value}\nThe value of self.tag is: {self.tag}\nThe value of self.children is: {self.children}\nThe value of self.props is: {self.props}")
        #a = formating_html(self.tag, self.value, self.props, self.children)
        return formating_html(self.tag, self.value, self.props, self.children)
        


class ParentNode(HTMLNode):

    def isParentNode(node):
        is_an_instance = isinstance(node, ParentNode)
        return(is_an_instance)


    def __init__(self, tag, children, props=None):
    # Note how we explicitly pass the parameters by name
        super().__init__(
            tag=tag,
            value=None,  # ParentNodes don't have values
            props=props,
            children=children
    )

    def to_html(self):
            
        def nodeStyle(node):
            if isinstance(node, LeafNode):
                return node.to_html()
            elif isinstance(node, ParentNode):
                return node.to_html()

        def handling_parent_node(children_list): #this function should return the prompt for the children 
            unfolding_children = "".join(map(nodeStyle, children_list))#this map function return an iterror that needs to be converter into a string and joined together 
        
            print(f"YOUR UNFOLDED CHILDREN: {unfolding_children}")
            return unfolding_children
        
        def formatting_parent_to_html(tag, children, props):
            print(f"I am printing from formatting_parent_to_html and tag is {tag}, chilren ia {children}")
            if tag == None or tag == '':
                raise ValueError("A ParentNode object must include a tag")
            if children == None or children == []:
                raise ValueError("A ParentNode must have children")
            
            html_prompt = f"<{tag}>{handling_parent_node(children)}</{tag}>"

            return html_prompt

        return formatting_parent_to_html(self.tag, self.children, self.props)

            


        
   
        