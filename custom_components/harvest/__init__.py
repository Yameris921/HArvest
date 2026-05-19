"""HArvest — Panneau d'export des entités vers Excel / CSV / JSON."""
import logging
from pathlib import Path

from homeassistant.core import HomeAssistant
from homeassistant.components.frontend import async_register_built_in_panel
from homeassistant.components.http import StaticPathConfig

_LOGGER = logging.getLogger(__name__)

DOMAIN = "harvest"
PANEL_URL = "/harvest_panel"
PANEL_PATH = "harvest"


async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    """Enregistre le chemin statique et le panneau latéral."""

    panel_dir = Path(__file__).parent / "panel"

    await hass.http.async_register_static_paths([
        StaticPathConfig(
            url_path=PANEL_URL,
            path=str(panel_dir),
            cache_headers=False,
        )
    ])

    async_register_built_in_panel(
        hass,
        component_name="iframe",
        sidebar_title="HArvest",
        sidebar_icon="mdi:sprout",
        frontend_url_path=PANEL_PATH,
        config={"url": f"{PANEL_URL}/index.html"},
        require_admin=False,
    )

    _LOGGER.info("HArvest : panneau enregistré sur %s/index.html", PANEL_URL)
    return True
