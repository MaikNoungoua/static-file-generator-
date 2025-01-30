from htmlnode import LeafNode, HTMLNode
from textnode import TextNode, TextType


def text_node_to_html_node(text_node):
    my_enum = [TextType.BOLD, TextType.TEXT, TextType.ITALIC, TextType.CODE, TextType.LINK, TextType.IMAGE]
    
    if text_node.text_type in my_enum : 
        match text_node.text_type:
            case TextType.TEXT:
                return LeafNode(None, text_node.text, None)
            
            case TextType.BOLD:
                return LeafNode("b", text_node.text, None)
            
            case TextType.ITALIC:
                return LeafNode("i", text_node.text, None)
            
            case TextType.CODE:
                return LeafNode("code", text_node.text, None)
            
            case TextType.LINK:
                props = {"href": text_node.url}
                return LeafNode("a", text_node.text, props)
                
            case TextType.IMAGE :
                props = {
                    "src": text_node.url,
                    "alt": text_node.text
                }
                return LeafNode("img", "", props)
                
            
    else: 
        raise Exception("One of the text the entered is not supported. \n Please refer to the to the README file to see the supported format")
            
            

        
