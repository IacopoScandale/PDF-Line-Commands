from .strings import COUNTER_JSON_NAME
from typing import NoReturn
import os
import sys
import json


def must_end_with_pdf(fname: str) -> str:
  """
  This function makes sure that input str `fname`
  ends or will be ending with ".pdf"
  """
  if not fname.endswith(".pdf"):
    return fname + ".pdf"
  return fname


def add_one_to_counter(command_name: str) -> None:
  """
  Call this function at the end of a command_file.py to
  add +1 usage to the counter. This counter will save
  how many times we use that command
  """
  here: str = os.path.dirname(os.path.abspath(__file__))
  full_path_counter_json: str = os.path.join(here, COUNTER_JSON_NAME)

  # create file if it does not exists
  if not os.path.exists(full_path_counter_json):
    print(f"Error: missing file {full_path_counter_json}")
    sys.exit()

  with open(full_path_counter_json, "r") as jsonfile:
    # load dictionary
    counter_json: dict[str,int] = json.load(jsonfile)
  # add +1 to the frequency dictionary
  if command_name not in counter_json:
    counter_json[command_name] = 1
  else:
    counter_json[command_name] += 1
  # save progress
  with open(full_path_counter_json, "w") as jsonfile:
    json.dump(counter_json, jsonfile, indent=2)


def choose_out_pdf_name() -> str | NoReturn:
  """
  This function lets you choose a pdf output name.
  - If the name already exists then it asks you whether to overvrite it.
    If your choice is No then it restarts so you can choose another name
  - If you want to exit just throw an KeyboardInterrupt exception just 
    press Ctrl+c on terminal

  ## Output
  `str` with a pdf name (that will end with '.pdf')

  """
  while True:
    try:
      input_pdf: str = input(
        "\nEnter output filename (it may or may not end with '.pdf')\n"
        "(press Ctrl+C (^C signal interrupt) to exit): "
      )
    except KeyboardInterrupt:
      print()
      sys.exit()

    pdf_name: str = must_end_with_pdf(input_pdf)

    # if the file already exists ask what to do
    if os.path.isfile(pdf_name):
      print(f"\nWarning: file '{pdf_name}' already exists,")
      overwrite_choice: str = input("do you want to overwrite it?\n[y,N]: ")
      # choice with No as default (because "" in "nN" is True)
      if overwrite_choice in "nN":
        pass
      elif overwrite_choice in "sSyY":
        return pdf_name
      
    else:
      return pdf_name