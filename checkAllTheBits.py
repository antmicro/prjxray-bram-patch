﻿# File: checkAllTheBits.py
# Author: Brent Nelson
# Created: 24 June 2020
# Description:
#    Driver to check all the designs in a directory for regression testing

import checkTheBits
import argparse
import pathlib

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "baseDir", help='Directory where design sub-directories are located.'
    )

    parser.add_argument("--verbose", action='store_true')

    parser.add_argument(
        "--printmappings", action='store_true', help='Print the mapping info'
    )

    args = parser.parse_args()

    baseDir = pathlib.Path(args.baseDir).resolve()
    dirs = list(baseDir.glob("*"))
    dirs.sort()

    for d in dirs:
        designName = d.name
        checkTheBits.checkTheBits(
            d, "mem/ram", d / "{}.mdd".format(designName), d / "init/init.mem",
            d / "real.fasm", args.verbose, args.printmappings
        )

    print("")

########################################################################
# Given a directory name, checkAllTheBits.py will run checkTheBits.py on
# every sub-directory in that directory.
# It is a way to get a full regression test using all the designs that were
#     generated by generate_tests.py
########################################################################
