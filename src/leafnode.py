from abc import ABC, abstractmethod
from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag: str | None = None, value: str | None = None, children = None, props: dict[str, str] | None = None) -> None:
        super().__init__(tag, value, None,  props)
    def __repr__(self) -> str:
        return f"{type(self).__name__}({self.tag}, {self.value}, {self.props})"
    def to_html(self) -> str:
        if not self.value:
            raise ValueError("All leaf nodes must contain a value")
        if self.tag == None:
            return f"{self.value}"
        if self.props:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
