"""Excel export functionality."""
from __future__ import annotations
import pandas as pd
import os

def write_xlsx(df: pd.DataFrame, path: str) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_excel(path, index=False, engine="openpyxl")
