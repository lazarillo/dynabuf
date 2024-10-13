import fire  # type: ignore # No type hints for fire


class Main:
    """dynabuf is a CLI tool for dynamically adding fields to protocol buffer messages.

    Usage:
        dynabuf add-field <input> <field>
    """

    def __init__(self):
        """Put options here in the constructor."""

    def add_field(self, input: str | int, field: str | int) -> str:
        """Can this be seen?"""
        return f"{input} has become {field}"


def main():
    fire.Fire(Main)
