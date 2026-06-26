"""
Copyright (c) 2026 IBM Corp.
SPDX-License-Identifier: Apache-2.0

spyremetrics - Python package for reading Spyre metric files in the new foramt
"""

from .metric_file import (
    FileHeader,
    MetricFile,
    MetricSection,
    SectionHeader,
)

from .section_type_defs import (
    MetricDataType,
    SectionType,
    SummarizerType,
    ValueType,
)

from .section_types import (
    CONFIG_FILE_LIST,
    config_version,
)

__version__ = "0.5.6"  ## TODO: Should refer to the package version
__all__ = [
    "CONFIG_FILE_LIST",
    "FileHeader",
    "MetricFile",
    "MetricSection",
    "SectionHeader",
    "MetricDataType",
    "SectionType",
    "SummarizerType",
    "ValueType",
    "config_version",
]

# Made with Bob
