from typing import List, Optional
from tqdm.autonotebook import tqdm
from multiprocessing.pool import ThreadPool


# Run tasks in parallel using Python’s multiprocessing module. Concurrency depends on the number of
# CPU cores available. This is useful for parallel inferencing, especially if the platform does not
# support it natively via API, like RITS.
def run_parallel(
    func,
    items,
    desc: Optional[str] = None,
    concurrency_limit: int = 10,
):
    outputs = []
    with ThreadPool(processes=concurrency_limit) as pool:
        for output in tqdm(
            pool.imap(func, items),
            total=len(items),
            desc=desc,
        ):
            outputs.append(output)

    return outputs
