from __future__ import annotations

import logging
import multiprocessing
import os
import sys

logging.basicConfig(level=logging.WARNING)


def main():
    multiprocessing.freeze_support()

    import randovania

    randovania.setup_logging("INFO", None, quiet=True)

    logging.debug("Starting Randovania...")

    # Add our local dotnet to path if it exists, which it only does for portable ones.
    dotnet_path = randovania.get_data_path().joinpath("dotnet_runtime")
    if dotnet_path.exists():
        os.environ["PATH"] = f'{dotnet_path}{os.pathsep}{os.environ["PATH"]}'
        os.environ["DOTNET_ROOT"] = f"{dotnet_path}"
        logging.debug("Portable dotnet path exists, added as DOTNET_ROOT.")

    from randovania import cli

    cli.run_cli(sys.argv)


if __name__ == "__main__":
    main()
