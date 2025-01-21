from textnode import TextNode, TextType
def main():
    node1 = TextNode("My beautiful first text", TextType.BOLD, "https://www.google.com")
    node2 = TextNode("My beautiful second text", TextType.ITALIC, "https://www.facebook.com")

    print(node1)
    print(node2)

    #print(f"My first node is: {node1_repr} \n My second node is: {node2_repr}")

if __name__ == "__main__" : 
    main()
