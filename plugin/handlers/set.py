from __future__ import annotations

import re
from typing import Unpack

import screen_brightness_control as sbc
from flogin import (
    ExecuteResponse,
    PlainTextCondition,
    Query,
    Result,
    SearchHandler,
)
from flogin.jsonrpc.results import ResultConstructorArgs

from ..conds import MultiAnyCondition
from ..plugin import ScreenBrightnessPlugin


class SetBrightnessResult(Result[ScreenBrightnessPlugin]):
    def __init__(
        self,
        value: int,
        monitor: str | None,
        kw: str,
        **kwargs: Unpack[ResultConstructorArgs],
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


class SetBrightnessHandler(SearchHandler[ScreenBrightnessPlugin]):
    def __init__(self):
        cond = MultiAnyCondition(*[PlainTextCondition(str(i + 1)) for i in range(100)])

        super().__init__(cond)

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
            )
