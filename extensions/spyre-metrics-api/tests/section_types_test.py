"""
Copyright (c) 2026 IBM Corp.
SPDX-License-Identifier: Apache-2.0

Test script to check if section and metric data type definitions can be loaded correctly.
"""

import sys
from traceback import print_tb, print_exception

"""
Try to import generated map of SectionType etc. objects
"""
try:
    from spyremetrics.generated_section_types import (
        MetricDataType,
        SectionType,
        SummarizerType,
        ValueType,
        VERSION,
        ## Singleton objetcts are added in the global map in generated_section_types.py
    )

    config_version = VERSION
    print("Loaded generated_section_types.py", file=sys.stderr)  # For debug
except ImportError as e:
    # For debug
    print(
        "Debug: Failed to import pre-converted config file. Fall back to load from JSON file",
        file=sys.stderr,
    )
    # print_tb(e.__traceback__, file=sys.stderr)
    print_exception(e, file=sys.stderr)

    """
    Load the config json file into a global map, so that SectionType etc. objects can be singleton
    """
    try:
        from spyremetrics import (
            MetricDataType,
            SectionType,
            SummarizerType,
            ValueType,
            config_version,
        )

        print("Loaded type definitions from JSON config", file=sys.stderr)  # For debug
    except Exception as e:
        print(f"ERROR: Excetion is thrown: {str(e)}", file=sys.stderr)
        print_tb(e.__traceback__, file=sys.stderr)
        sys.exit(1)

print(f"Config version: {config_version}")
for n, c in {
    "Section": SectionType,
    "Metric": MetricDataType,
    "Value": ValueType,
    "Summarizers": SummarizerType,
}.items():
    print(f"=== {n} type ===")
    print(*[str(e) for e in c.items()], sep="\n")
