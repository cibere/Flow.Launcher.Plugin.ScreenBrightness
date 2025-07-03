from __future__ import annotations

from flogin import PlainTextCondition, ProgressBar, Query, Result, SearchHandler

from ..plugin import ScreenBrightnessPlugin
import random


class GetBrightnessHandler(SearchHandler[ScreenBrightnessPlugin]):
    def __init__(self):
        super().__init__(PlainTextCondition(""))

    async def callback(self, query: Query):
        assert self.plugin

        for value, monitor in self.plugin.get_brightnesses():
            yield Result(
                "",
                sub=f"Monitor: {monitor} | Brightness: {value}%",
                icon="assets/app.png",
                progress_bar=ProgressBar(value, "#f7f309"),
                auto_complete_text="".join(
                    random.choices("qwertyuiopasdfghjkl;zxcvbnm")
                ),
            )
