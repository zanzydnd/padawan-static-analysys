import logging
from typing import List

from radon.metrics import mi_visit

logger = logging.getLogger(__name__)


def mi_metrics(
        files_paths: List[str],
        remove_prefix: str,
        data: dict
):
    mi_indexes = {}

    for file in files_paths:
        with open(file, 'r') as f:
            file_content = f.read()
            logger.info(file)
            logger.info(mi_visit(file_content, multi=True))
            data[
                file.replace(remove_prefix, '')
            ]['mi_index'] = mi_visit(file_content, multi=True)
    return mi_indexes
