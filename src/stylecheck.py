import re
import logging
from copy import deepcopy
from io import StringIO
from typing import List

from pylint.lint import Run
from pylint.reporters.text import TextReporter

logger = logging.getLogger(__name__)


def style_check(
        files: List[str],
        remove_prefix: str,
        data: dict
):
    result = {
        'duplicates_count': 0,
        'conventions_count': 0
    }

    pylint_output = StringIO()
    reporter = TextReporter(pylint_output)

    args = deepcopy(files)

    args.append("--disable=all")
    args.append("--enable=C")
    args.append("--enable=R0801")
    args.append("--disable=C0103,C2001,C1901,C0209")
    logger.info(args)
    Run(args, reporter, do_exit=False)

    pattern = r"\bR0801"
    duplicates_count = len(re.findall(pattern, pylint_output.getvalue()))

    pattern = r"(module_\d+/task_\w+.py):\d+:\d+: C\d+:"
    conventions_count = len(set(re.findall(pattern, pylint_output.getvalue())))
    logger.info(f'full pylint {pylint_output.getvalue()}')
    data['duplicates_count'] = duplicates_count
    data['conventions_count'] = conventions_count
