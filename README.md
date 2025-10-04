# SKU Row Consolidator

A simple Python utility that merges multiple rows with the same `SKU` into a single row by combining **all non-empty values** from each column.

Useful for cleaning product data exports (for example, WooCommerce or ERP CSVs) where the same SKU appears multiple times with partial data spread across rows.

---

## 📋 Features

- Combines **all non-empty values** across rows with the same SKU  
- Keeps the **original column order**  
- Removes **duplicate values** in merged fields  
- Uses a customizable separator (default: `|`)  
- Supports UTF-8 CSVs (including BOM: `utf-8-sig`)  
- Creates one clean row per unique SKU  

---

## 🧠 Example

### Input (`input.csv`)
```csv
SKU,A1,A2,A3
1,2,,
1,,3,
1,,,5
2,10,20,
2,10,,30
```

### Output (output.csv)
```
SKU,A1,A2,A3
1,2,3,5
2,10,20,30
```

### Installation

pip install pandas

git clone https://github.com/yourusername/sku-row-consolidator.git
cd sku-row-consolidator

### Usage

python combine_sku_rows.py

By default, it reads from input.csv and writes the combined result to output.csv.

You can also specify custom file names and encoding by editing the function call at the bottom of the script:

if __name__ == "__main__":
    consolidate_all_values(
        input_csv="your_file.csv",
        output_csv="merged.csv",
        sku_col="SKU",
        encoding="utf-8-sig"
    )

### Requirements

Python ≥ 3.8

pandas ≥ 1.3
