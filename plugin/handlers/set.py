from __future__ import annotations

import re, random
from typing import Unpack

import screen_brightness_control as sbc
from flogin import (
    ExecuteResponse,
    PlainTextCondition,
    Query,
    Result,
    SearchHandler,
    ResultConstructorKwargs,
    AnyCondition,
)

from ..plugin import ScreenBrightnessPlugin


class SetBrightnessResult(Result[ScreenBrightnessPlugin]):
    def __init__(
        self,
        value: int,
        monitor: str | None,
        kw: str,
        **kwargs: Unpack[ResultConstructorKwargs],
    ):
        super().__init__(**kwargs)

        self.value = value
        self.kw = kw
        self.monitor = monitor

    async def callback(self):
        assert self.plugin

        self.plugin.set_brightness(self.value, monitor=self.monitor)
        await self.plugin.api.show_notification(
            "ScreenBrightness",
            (
                f"Successfully set the brightness of your {self.monitor} display to {self.value}%."
                if self.monitor
                else f"Successfully set the brightness of all of your displays to {self.value}%."
            ),
        )
        await self.plugin.api.change_query(f"{self.kw} ")

        return ExecuteResponse(False)


AnyNumberCondition = AnyCondition(*[PlainTextCondition(str(i + 1)) for i in range(100)])


class SetBrightnessHandler(SearchHandler[ScreenBrightnessPlugin]):
    def __init__(self):
        super().__init__(AnyNumberCondition)

    async def callback(self, query: Query[re.Match]):
        assert self.plugin

        value = int(query.text.strip())

        yield SetBrightnessResult(
            value,
            None,
            title=f"Set brightness to {value}% for all of your displays?",
            icon="assets/app.png",
            kw=query.keyword,
            score=10,
        )

        for monitor in sbc.list_monitors():
            yield SetBrightnessResult(
                value,
                monitor,
                title=f"Set brightness to {value}% for {monitor}?",
                icon="assets/app.png",
                kw=query.keyword,
                auto_complete_text="".join(
                    random.choices("qwertyuiopasdfghjkl;zxcvbnm")
                ),
            )
