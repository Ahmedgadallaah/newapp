[project]
name = "Maintenance Network Contract"
authors = [
    { name = "ahmedgadallaah", email = "support@ahmed.com"}
]
description = "Enwan  network Contract"
requires-python = ">=3.10"
readme = "README.md"
dynamic = ["version"]
dependencies = [
    # "frappe~=15.0.0" # Installed and managed by bench.
]

[build-system]
requires = ["flit_core >=3.4,<4"]
build-backend = "flit_core.buildapi"

# These dependencies are only installed when developer mode is enabled
[tool.bench.dev-dependencies]
# package_name = "~=1.1.0"
