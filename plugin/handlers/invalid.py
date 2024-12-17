from __future__ import annotations

import re
from flogin import Query, Result, SearchHandler

from ..plugin import ScreenBrightnessPlugin


class InvalidSetBrightnessHandler(SearchHandler[ScreenBrightnessPlugin]):
    async def callback(self, query: Query[re.Match]):
        return Result(
            "Invalid Brightness Value. Brightness value must be a valid whole number from 0 to 100.",
            icon="assets/error.png",
        )
