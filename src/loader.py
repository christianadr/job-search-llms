from pathlib import Path

import pandas as pd

from src.constants import globals as g


def load_joblistings(path: Path) -> pd.DataFrame:
    dfs = list()

    files = g.DATA_DIR.glob("*.json")

    for file in files:
        temp_df = pd.read_json(Path(g.DATA_DIR, file))
        dfs.append(temp_df)
        # print(Path(g.DATA_DIR, file))

    df = pd.concat(dfs, ignore_index=True)

    return df
