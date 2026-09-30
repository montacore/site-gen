from htmlnode import HTMLNode

class ParentNode(HTMLNode):

    def __init__(self, tag: str, children: list[HTMLNode], props: dict[str, str] | None=None):
        super().__init__(tag, None, children, props)

    def to_html(self) -> str:
        if not self.tag:
            raise ValueError("No tag provided for node")
        if self.children == None:
            raise ValueError("node has no children, not a Parent Node")
        if self.props:
            return f"<{self.tag}{self.props_to_html}>"
