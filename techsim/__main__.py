#!/usr/bin/env python3
"""Startup script for the bot.

This script is used to start the bot.
We don't really need to do anything here, so we just call the bot's startup
function.

Typical usage example:
    $ python3 techsim
    OR
    $ poetry run start
"""
# License: EPL-2.0
# SPDX-License-Identifier: EPL-2.0
# Copyright (c) 2023-present Tech. TTGames

import asyncio
import sys

import techsim
from techsim.data import config
from techsim.data import const


def main():
    """Starts the bot.

    This function is the entry point for the bot.
    """
    print(f"Starting TechSim {const.VERSION}...")
    cnfg = config.Config()
    print("Brace for timeloop!")
    debug_mode = 'pydevd' in sys.modules
    asyncio.run(techsim.start_bot(conf=cnfg, debug=debug_mode), debug=debug_mode)


if __name__ == "__main__":
    main()
