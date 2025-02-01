from __future__ import annotations

import dataclasses
from typing import NamedTuple

from randovania.bitpacking.json_dataclass import EXCLUDE_DEFAULT, JsonDataclass


class HintDetails(NamedTuple):
    determiner: str
    description: str


@dataclasses.dataclass(frozen=True, order=True)
class HintFeature(JsonDataclass):
    name: str = dataclasses.field(metadata={"init_from_extra": True})
    long_name: str
    hint_details: HintDetails = dataclasses.field(metadata={"store_named_tuple_without_names": True})

    def __post_init__(self) -> None:
        assert self.name, "Name must not be empty"
        assert self.long_name, "Long name must not be empty"

    @property
    def general_details(self) -> HintDetails:
        # FIXME
        return HintDetails("an ", "item")

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}')"


@dataclasses.dataclass(frozen=True, order=True)
class PickupHintFeature(HintFeature):
    is_broad_category: bool = dataclasses.field(default=False, metadata=EXCLUDE_DEFAULT)
    """Used for Echoes Flying Ing Cache hints"""

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}')"
