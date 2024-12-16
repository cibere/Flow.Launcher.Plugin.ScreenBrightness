from flogin import Plugin

from .settings import ScreenBrightnessSettings
import screen_brightness_control as sbc

class ScreenBrightnessPlugin(Plugin[ScreenBrightnessSettings]):
    def __init__(self) -> None:
        super().__init__()

        from .handlers.get import GetBrightnessHandler
        from .handlers.invalid import InvalidSetBrightnessHandler
        from .handlers.set import SetBrightnessHandler
        
        self.register_search_handlers(SetBrightnessHandler(), GetBrightnessHandler(), InvalidSetBrightnessHandler())
    
    @property
    def brightness(self) -> int:
        return sbc.get_brightness()[0]
    
    @brightness.setter
    def brightness(self, value: int) -> None:
        sbc.set_brightness(value)