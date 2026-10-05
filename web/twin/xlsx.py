"""Eksport XLSX z neutralizacją formuł (CSV/formula injection)."""
import io

from django.http import HttpResponse

_FORMULA_PREFIXES = ("=", "+", "-", "@", "\t", "\r")


def safe_cell(v):
    """Tekst zaczynający się od = + - @ TAB CR → prefiks `'`. Liczby bez zmian."""
    if isinstance(v, str) and v.startswith(_FORMULA_PREFIXES):
        return "'" + v
    return v


def _make_xlsx_response(filename: str):
    """(workbook, worksheet, HttpResponse) gotowe do wypełnienia."""
    import openpyxl
    wb = openpyxl.Workbook()
    response = HttpResponse(content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response["Content-Disposition"] = f'attachment; filename="{filename}"'
    return wb, wb.active, response


def _finalize_xlsx(wb, ws, response):
    for sheet in wb.worksheets:
        for row in sheet.iter_rows():
            for c in row:
                if c.data_type == "f" and isinstance(c.value, str):
                    c.value = safe_cell(c.value)
    buf = io.BytesIO()
    wb.save(buf)
    response.content = buf.getvalue()
    return response
