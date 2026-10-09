from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    """
    Data Class for a HTMLNode with no children, all LeafNodes **must** have values
    otherwise a ValueError is raised. tags and props are optional.
    Each value is passed directly from parent class HTMLNode
    """
    def __init__(self, tag: str | None, value: str | None, props: dict[str, str] | None = None) -> None:
        super().__init__(tag, value, None,  props)

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self.tag}, {self.value}, {self.props})"

    def to_html(self) -> str:
        """
            to_html() overrides parent method to_html to handle parsing html nodes
            in the event the node is a leaf(has no chilren)
            this method prevents the parsing of the node if it does not contain
            a value. 
            If no tag is present a raw string is returned.
            If props are passed then they are handled with parent method props_to_html
            
        """
        if self.value == None:
            raise ValueError("All leaf nodes must contain a value")
        if self.tag == None:
            return f"{self.value}"
        if self.props:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        return f"<{self.tag}>{self.value}</{self.tag}>"
