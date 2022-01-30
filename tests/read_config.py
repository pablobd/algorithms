from abc import ABC
from dataclasses import dataclass
from pathlib import Path
from typing import List

import yaml
from black import Optional, Type


@dataclass
class Config(ABC):
    def __new__(cls, *args, **kwargs):
        if cls == Config:
            raise TypeError("Cannot instantiate abstract class.")
        return super().__new__(cls)


def get_names(base_names: List[str], test_name: Optional[str] = None) -> List[str]:
    if test_name:
        return base_names + [test_name]
    else:
        return base_names


def read_config(params_class: Type[Config], nested_names: List[str]):
    with open(Path(__file__).resolve().parent / "config.yaml") as f:
        conf = yaml.load(f, Loader=yaml.Loader)
    for name in nested_names:
        conf = conf[name]
    return params_class(**conf)
