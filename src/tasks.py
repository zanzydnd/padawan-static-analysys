import logging
import time

from typing import List
from uuid import uuid4

import requests

from src.analyzer import AnayzerRunner
from src.core.complexity import mi_metrics
from src.accessors import GitAccessor
from src.celery_farmer import celery_app
from src.stylecheck import style_check

logger = logging.getLogger(__name__)


# celery --app src.celery_farmer worker --loglevel=info -Q static -n static_analysis
def prepare(git_url: str, ident: str):
    git_accessor = GitAccessor()
    git_accessor.pull_repository(git_url, ident)

    return git_accessor


def clean_up(ident: str, git_accessor: GitAccessor):
    git_accessor.delete_local_repository(ident)


@celery_app.task(name='static.static_analysis')
def check_student_solution(
        submission_id: int,
        analysis_steps: List[str],
        git_url: str
):
    ident = str(uuid4())[:8]

    git_accessor = prepare(git_url, ident)
    time.sleep(10)
    analyzer = AnayzerRunner(ident)
    analyzer.run()
    result = {**analyzer.filename_to_analyzer_result, **analyzer.stats}
    style_check(
        analyzer.files_paths,
        remove_prefix=analyzer.root_dr,
        data=result
    )
    mi_metrics(
        analyzer.files_paths,
        remove_prefix=analyzer.root_dr,
        data=result
    )
    logger.info(result)
    clean_up(ident, git_accessor)
    requests.post(
        f"http://127.0.0.1:8000/api/v1/submission_static_analysis/{submission_id}/",
        json=result
    )
