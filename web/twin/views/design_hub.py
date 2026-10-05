# Ekran „Projektowanie magazynu”: ścieżka 7 kroków od generatora hali do porównania wariantów.
from twin.models_tasks import WarehouseTaskBatch
from twin.shared import _planner, render

__all__ = ["design_hub"]

_STEPS_AFTER_IMPORT = [(3, "Dzień projektowy"), (4, "Kalibracja na obecnej hali"), (5, "Prognoza wzrostu"),
                       (6, "Symulacja dnia"), (7, "Porównanie wariantów")]


@_planner
def design_hub(request):
    return render(request, "twin/design_hub.html", {
        "design_batch": WarehouseTaskBatch.objects.filter(status="done").first(),
        "design_steps_off": [(n, t, "Po imporcie zadań magazynowych.") for n, t in _STEPS_AFTER_IMPORT],
    })
