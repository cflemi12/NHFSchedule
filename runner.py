from openpyxl import load_workbook

wb = load_workbook("practice.xlsx", read_only=True)
ws = wb.active
