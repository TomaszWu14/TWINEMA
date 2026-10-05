# Widoki bliźniaka magazynu — re-eksport modułów (urls.py odwołuje się przez `views.<nazwa>`).
from .bay_templates import *  # noqa: F401,F403
from .design_hub import *  # noqa: F401,F403
from .warehouse_blender import *  # noqa: F401,F403
from .warehouse_calibration import *  # noqa: F401,F403
from .warehouse_compare import *  # noqa: F401,F403
from .warehouse_design_day import *  # noqa: F401,F403
from .warehouse_design_sim import *  # noqa: F401,F403
from .warehouse_forecast import *  # noqa: F401,F403
from .warehouse_generator import *  # noqa: F401,F403
from .warehouse_model import *  # noqa: F401,F403
from .warehouse_model_ewm import *  # noqa: F401,F403
from .warehouse_racktype import *  # noqa: F401,F403
from .warehouse_tasks import *  # noqa: F401,F403
from .warehouse_variant_edit import *  # noqa: F401,F403
from .warehouse_variants import *  # noqa: F401,F403
