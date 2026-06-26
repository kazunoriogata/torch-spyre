"""
Copyright (c) 2026 IBM Corp.
SPDX-License-Identifier: Apache-2.0

Wrapper to access Spyre metric file in the old format.
"""

import sys

from pathlib import Path
from typing import Iterable

# Assuming config json files are already loaded
from .section_types import MetricDataType

## Add pre-defined import path, and import APIs from libaiusmi.so
sys.path.insert(0, str(Path("~/.local/lib").expanduser()))
sys.path += ["/opt/ibm/sys/spyre/aiu-monitor/lib", "/opt/ibm/sys/spyre/runtime/lib"]

try:
    from libaiumonitor import DcrHelper, Snapshot
except ImportError as e:
    print(
        "ERROR: Failed to load libaiuminotor.so. Check if ibm-aiu-monitor RPM is installed and/or LD_LIBRARY_PATH is set correctly.",
        file=sys.stderr,
    )
    raise RuntimeError(
        "Missing libaiumonitor.so to handle metrics file in the old format"
    ) from e

dummy = DcrHelper.calculate(None, None)
counters = DcrHelper.setupCounters(None)

dtype_names = ["pwr", "tempr", "rdmem", "wrmem", "rxpci", "txpci", "rdrdma", "wrrdma"]
dtype_list = [MetricDataType.find_by_name(n) for n in dtype_names]


def read_old_metrics(path: Path | str) -> Iterable[tuple[MetricDataType, int | float]]:
    snapshot = Snapshot(path)
    values = DcrHelper.calculate(counters[0].value(snapshot), dummy)

    for i, data_type in enumerate(dtype_list):
        yield data_type, values[i]
