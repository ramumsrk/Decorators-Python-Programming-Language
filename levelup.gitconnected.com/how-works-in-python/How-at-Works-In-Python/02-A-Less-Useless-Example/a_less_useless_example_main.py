#! /usr/bin/python3.12

from pathlib import Path

import logging

# Logging configuration
logging.basicConfig(
  level=logging.DEBUG,
  format="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
  datefmt="%Y-%m-%s %H:%M:%S.%s",
  filemode='+a',
  filename=F'{Path(__file__).parent.parent}/logs/a_less_useless_example.log'
)

from a_less_useless_example.a_less_useless_example import add_exclamation

from typing import Literal

# User-defined function
@add_exclamation
def hi(
  sample_input_name: Literal[str]
) -> Literal[str]:
  return f'Hello, {sample_input_name}'

if __name__ == '__main__':

  logging.debug(
    f'{hi("tom")}'
  )