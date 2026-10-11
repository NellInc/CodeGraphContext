import pytest

from codegraphcontext.utils.tree_sitter_manager import TreeSitterManager


@pytest.mark.parametrize("alias", ["c_sharp", "csharp", "c#", "cs"])
def test_csharp_alias_loads_and_parses(alias):
    """C# comes from the declared language pack, with one shared cache entry."""
    manager = TreeSitterManager()
    language = manager.get_language_safe(alias)
    assert manager.get_language_safe("c_sharp") is language
    assert list(manager._language_cache) == ["c_sharp"]
    tree = manager.create_parser(alias).parse(b"class Greeter { void Hello() {} }")
    assert not tree.root_node.has_error
    assert tree.root_node.named_children[0].type == "class_declaration"
