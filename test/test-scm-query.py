from tree_sitter import Language, Parser

# Setup parser
from tree_sitter_languages import get_language
fsharp_language = get_language('fsharp')
parser = Parser()
parser.set_language(fsharp_language)

# Load and parse any F# source code
source_code = """
module MyModule

let add x y = x + y

type Person = {
    Name: str
    Age: Int
}

let main () =
    let person = { Name = "John" }
    add 1 2
"""

# Parse the source
tree = parser.parse(bytes(source_code, "utf8"))

# Load and try individual query patterns to test them
def test_query(pattern):
    try:
        query = fsharp_language.query(pattern)
        matches = query.captures(tree.root_node)
        print(f"\nTesting pattern: {pattern}")
        for match in matches:
            capture, node = match
            print(f"Match found: {capture} -> {node}")
    except Exception as e:
        print(f"Error in pattern: {pattern}")
        print(f"Error message: {str(e)}")

# Test individual patterns
test_query("(named_module name: (long_identifier) @name.definition.module) @definition.module")
test_query("(type_definition name: (identifier) @name.definition.class) @definition.class")
