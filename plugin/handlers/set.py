from __future__ import annotations

from flogin import Query, Result, SearchHandler, ExecuteResponse, PlainTextCondition, MultiCondition
from flogin.jsonrpc.results import ResultConstructorArgs
from typing import Unpack
from ..plugin import ScreenBrightnessPlugin
import re
from ..conds import MultiAnyCondition

class SetBrightnessResult(Result[ScreenBrightnessPlugin]):
    def __init__(self, value: int, kw: str, **kwargs: Unpack[ResultConstructorArgs]):
        super().__init__(**kwargs)

        self.value = value
        self.kw = kw

    async def callback(self):
        assert self.plugin

        self.plugin.brightness = self.value
        await self.plugin.api.show_notification("ScreenBrightness", f"Successfully set screen brightness to {self.value}%.")
        await self.plugin.api.change_query(f"{self.kw} ")
        
        return ExecuteResponse(False)

class SetBrightnessHandler(SearchHandler[ScreenBrightnessPlugin]):
    def __init__(self):
        cond = MultiAnyCondition(*[PlainTextCondition(str(i + 1)) for i in range(100)])

        super().__init__(cond)

    async def callback(self, query: Query[re.Match]):
        assert self.plugin

        value = int(query.text.strip())
        
        return SetBrightnessResult(value, title=f"Set brightness to {value}%?", icon="assets/app.png", kw=query.keyword)