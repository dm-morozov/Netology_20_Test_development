from typing import List


def fio(initials: List[str]) -> str:
  fio = ''
  for item in initials:
    fio += item[0]
  return fio