


class HTMLNode:
    def __init__(self, tag: str | None=None, value: str | None=None, children: list["HTMLNode"] | None=None, props: dict[str, str] | None=None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        return f"{type(self).__name__}({self.tag}, {self.value}, {self.children}, {self.props})"

    def to_html(self) -> None:
        raise NotImplementedError

    def props_to_html(self) -> str:
        res = ""
        if self.props == None:
            return ""
        for k, v in self.props.items():
            res += f' {k}="{v}"'
        return res
