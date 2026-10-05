# Prognoza wzrostu z historii zadań EWM (plan 2026-10-02, etap 5): tempo roczne P50/P90 per strumień,
# mnożnik na horyzont lat, test wsteczny (MAPE) → mnożnik prosto do symulacji / porównania wariantów.
from urllib.parse import urlencode

from django.core.cache import cache

from twin.shared import _planner, get_object_or_404, render
from twin.design_day import load_inputs
from twin.design_forecast import BACKTEST_WEEKS, MIN_WEEKS, forecast
from twin.models_tasks import WarehouseTaskBatch
from twin.views.warehouse_design_day import CACHE_TTL
from twin.views.warehouse_design_sim import _int

__all__ = ["ewm_tasks_forecast"]


@_planner
def ewm_tasks_forecast(request, pk):
    batch = get_object_or_404(WarehouseTaskBatch, pk=pk, status="done")
    years = _int(request.GET.get("years"), 5, 1, 20)
    inputs = cache.get_or_set(f"wt-profile-inputs:{batch.pk}", lambda: load_inputs(batch), CACHE_TTL)
    rows = forecast(inputs["daily"], years)
    total = next((r for r in rows if r["key"] == "total"), None)
    links = {s: "?" + urlencode({"p": 95, "mult": total[f"mult_{s}"]}) for s in ("p50", "p90")} if total else {}
    return render(request, "twin/ewm_tasks/forecast.html", {
        "batch": batch, "years": years, "rows": rows, "total": total, "links": links,
        "backtest_weeks": BACKTEST_WEEKS, "min_weeks": MIN_WEEKS,
    })
