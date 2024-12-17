from typing import Iterable

import screen_brightness_control as sbc
from flogin import Plugin

from .settings import ScreenBrightnessSettings


class ScreenBrightnessPlugin(Plugin[ScreenBrightnessSettings]):
    def __init__(self) -> None:
        super().__init__()

        from .handlers.get import GetBrightnessHandler
        from .handlers.invalid import InvalidSetBrightnessHandler
        from .handlers.set import SetBrightnessHandler

        self.register_search_handlers(
            SetBrightnessHandler(),
            GetBrightnessHandler(),
            InvalidSetBrightnessHandler(),
        )

    def get_brightnesses(self) -> Iterable[tuple[int, str]]:
        return zip(sbc.get_brightness(), sbc.list_monitors())

    def set_brightness(self, value: int, monitor: int | str | None = None) -> None:
        sbc.set_brightness(value, display=monitor)
