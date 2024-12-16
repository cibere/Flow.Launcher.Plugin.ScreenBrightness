from __future__ import annotations

from flogin import Query, Result, SearchHandler, PlainTextCondition, ProgressBar

from ..plugin import ScreenBrightnessPlugin


class GetBrightnessHandler(SearchHandler[ScreenBrightnessPlugin]):
    def __init__(self):
        super().__init__(PlainTextCondition(""))

    async def callback(self, query: Query):
        assert self.plugin

        return Result("", sub=f"Brightness: {self.plugin.brightness}%", icon="assets/app.png", progress_bar=ProgressBar(self.plugin.brightness, "#f7f309"))