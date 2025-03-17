from textnode import *
from htmlnode import HTMLNode

def main():
    dummy = TextNode("this is some anchor text", TextType.LINK, "https://www.boot.dev")
    dummy2 = HTMLNode("p", "this is the text inside the tag", None, {"href": "https://www.google.com","target": "_blank"})
    print(dummy2)


if __name__ =="__main__":
    main()
