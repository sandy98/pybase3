#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import inspect
import importlib

def generate_markdown(module_name):
    # Import the module
    module = importlib.import_module(module_name)
    
    # Start building the markdown content
    markdown = f"# {module_name} Documentation\n\n"
    markdown += "This documentation is generated from the docstrings in the module.\n\n"

    for name, obj in inspect.getmembers(module):
        if inspect.isclass(obj):
            markdown += f"## Class: `{name}`\n\n"
            doc = inspect.getdoc(obj)
            markdown += f"{doc or 'No documentation available.'}\n\n"
            
            # Include methods
            for method_name, method_obj in inspect.getmembers(obj, inspect.isfunction):
                markdown += f"### Method: `{method_name}`\n\n"
                method_doc = inspect.getdoc(method_obj)
                markdown += f"{method_doc or 'No documentation available.'}\n\n"
                
        elif inspect.isfunction(obj):
            markdown += f"## Function: `{name}`\n\n"
            doc = inspect.getdoc(obj)
            markdown += f"{doc or 'No documentation available.'}\n\n"

    return markdown

# Generate Markdown for the pybase3 module
module_name = "pybase3"  # Replace with your module's name
markdown_content = generate_markdown(module_name)

# Save the Markdown to a file
output_file = "docs/pybase3.md"
with open(output_file, "w") as f:
    f.write(markdown_content)

print(f"Documentation saved to {output_file}")

