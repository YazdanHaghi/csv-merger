import pandas as pd

def collect_nonempty(series, sep="|"):
    """Collect all unique non-empty values in a column, join with sep."""
    values = [str(v).strip() for v in series if pd.notna(v) and str(v).strip() != ""]
    # keep order, remove duplicates
    seen = set()
    collected = [x for x in values if not (x in seen or seen.add(x))]
    return sep.join(collected) if collected else pd.NA

def consolidate_all_values(
    input_csv: str,
    output_csv: str = "output.csv",
    sku_col: str = "SKU",
    encoding: str = "utf-8-sig"
):
    df = pd.read_csv(input_csv, dtype={sku_col: str}, encoding=encoding)

    # strip strings and normalize
    for col in df.columns:
        if df[col].dtype == object:
            df[col] = df[col].astype(str).str.strip()
            df[col] = df[col].replace({"nan": pd.NA, "NaN": pd.NA, "None": pd.NA, "": pd.NA})

    cols = list(df.columns)
    if sku_col not in cols:
        raise ValueError(f"'{sku_col}' column not found.")

    grouped = df.groupby(sku_col, sort=False)

    agg_dict = {col: (lambda s, colname=col: collect_nonempty(s))
                for col in cols if col != sku_col}
    consolidated = grouped.agg(agg_dict).reset_index()

    consolidated.to_csv(output_csv, index=False, encoding=encoding)
    print(f"✅ Consolidated CSV written to: {output_csv}")

if __name__ == "__main__":
    consolidate_all_values("input.csv", output_csv="output.csv")
