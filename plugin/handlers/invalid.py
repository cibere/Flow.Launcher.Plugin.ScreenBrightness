from __future__ import annotations

from flogin import Query, Result, SearchHandler, ExecuteResponse, RegexCondition
from flogin.jsonrpc.results import ResultConstructorArgs
from typing import Unpack
from ..plugin import ScreenBrightnessPlugin
import re

class InvalidSetBrightnessHandler(SearchHandler[ScreenBrightnessPlugin]):
    async def callback(self, query: Query[re.Match]):
        return Result("Invalid Brightness Value. Brightness value must be a valid whole number from 0 to 100.", icon="assets/app.png")