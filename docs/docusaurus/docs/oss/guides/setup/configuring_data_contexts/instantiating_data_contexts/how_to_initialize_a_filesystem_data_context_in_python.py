"""
To run this code as a local test, use the following console command:
```
pytest -v --docs-tests -k "how_to_initialize_a_filesystem_data_context_in_python" tests/integration/test_script_runner.py
```
"""

import pathlib

import great_expectations as gx
from great_expectations.data_context.data_context.file_data_context import (
    FileDataContext,
)

# Python
# <snippet name="docs/docusaurus/docs/oss/guides/setup/configuring_data_contexts/instantiating_data_contexts/how_to_initialize_a_filesystem_data_context_in_python.py path_to_empty_folder">
path_to_empty_folder = "/my_gx_project/"
# </snippet>

project_root_dir = pathlib.Path.cwd().absolute()
path_to_context_root_folder = project_root_dir / FileDataContext.GX_DIR

path_to_empty_folder = project_root_dir

# Python
# <snippet name="docs/docusaurus/docs/oss/guides/setup/configuring_data_contexts/instantiating_data_contexts/how_to_initialize_a_filesystem_data_context_in_python.py initialize_filesystem_data_context">
from great_expectations.data_context import FileDataContext

context = gx.get_context(mode="file", project_root_dir=path_to_empty_folder)
# </snippet>

assert context
assert context.root_directory == str(path_to_context_root_folder)
