import typer
from pathlib import Path
from typing import Annotated


def main(input_path: Annotated[Path, typer.Argument(help="Path to the folder")]):
    print("doing something")


if __name__ == "__main__":
    typer.run(main)
