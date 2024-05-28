#! /usr/bin/python3.12

from typing import Literal

# User-defined decorator
def add_exclamation(
  function_reference: callable
) -> callable:
  # User-defined nested or inner function
  def wrapper(sample_input_name: str) -> callable:
    return F'{function_reference(sample_input_name)}!'
  return wrapper