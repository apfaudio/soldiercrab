#!/usr/bin/env python3
"""Compare designator -> footprint mapping between the KiCad BOM csv and a
JLCPCB .xls BOM. Reports any discrepancy in either direction.

Usage:
    python3 compare_bom.py [BOM-soldiercrab.csv] [bom.xls]
"""
import csv
import sys
import os

DEFAULT_CSV = os.path.join(os.path.dirname(__file__), "BOM-soldiercrab.csv")
DEFAULT_XLS = os.path.expanduser("~/Downloads/bom(11).xls")


def split_designators(field):
    return [d.strip() for d in field.split(",") if d.strip()]


def load_csv(path):
    """Return {designator: (footprint, lcsc)} from the KiCad csv."""
    mapping = {}
    with open(path, newline="") as f:
        for row in csv.DictReader(f):
            if not row.get("Designator"):
                continue
            fp = (row.get("Footprint") or "").strip()
            lcsc = (row.get("LCSC") or "").strip()
            for d in split_designators(row["Designator"]):
                mapping[d] = (fp, lcsc)
    return mapping


def load_xls(path):
    """Return {designator: (footprint, lcsc)} from the JLCPCB .xls (top+bottom)."""
    import xlrd

    mapping = {}
    sh = xlrd.open_workbook(path).sheet_by_index(0)
    header = [str(c).strip() for c in sh.row_values(0)]
    col = {name: header.index(name) for name in header}
    fp_i = col["Footprint"]
    lcsc_i = col["JLCPCB Part #"]
    desig_cols = [col[c] for c in ("topDesignator", "bottomDesignator") if c in col]
    for r in range(1, sh.nrows):
        row = sh.row_values(r)
        fp = str(row[fp_i]).strip()
        lcsc = str(row[lcsc_i]).strip()
        for ci in desig_cols:
            for d in split_designators(str(row[ci])):
                mapping[d] = (fp, lcsc)
    return mapping


def main():
    csv_path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_CSV
    xls_path = sys.argv[2] if len(sys.argv) > 2 else DEFAULT_XLS

    a = load_csv(csv_path)
    b = load_xls(xls_path)
    a_name = os.path.basename(csv_path)
    b_name = os.path.basename(xls_path)

    all_desigs = sorted(set(a) | set(b), key=lambda s: (s[:1], int("".join(filter(str.isdigit, s)) or 0)))

    only_a, only_b, fp_mismatch, lcsc_mismatch = [], [], [], []
    for d in all_desigs:
        if d not in b:
            only_a.append(d)
        elif d not in a:
            only_b.append(d)
        else:
            if a[d][0] != b[d][0]:
                fp_mismatch.append(d)
            if a[d][1] != b[d][1]:
                lcsc_mismatch.append(d)

    print(f"Comparing designator -> footprint / LCSC part")
    print(f"  A = {a_name} ({len(a)} designators)")
    print(f"  B = {b_name} ({len(b)} designators)")
    print()

    if only_a:
        print(f"Only in A ({a_name}):")
        for d in only_a:
            print(f"  {d:8} {a[d][0]}  {a[d][1]}")
        print()
    if only_b:
        print(f"Only in B ({b_name}):")
        for d in only_b:
            print(f"  {d:8} {b[d][0]}  {b[d][1]}")
        print()
    if fp_mismatch:
        print("Footprint mismatch:")
        for d in fp_mismatch:
            print(f"  {d:8} A={a[d][0]}  B={b[d][0]}")
        print()
    if lcsc_mismatch:
        print("LCSC part mismatch:")
        for d in lcsc_mismatch:
            print(f"  {d:8} A={a[d][1]}  B={b[d][1]}")
        print()

    if not (only_a or only_b or fp_mismatch or lcsc_mismatch):
        print("No discrepancies: designator -> footprint and LCSC match in both files.")
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
