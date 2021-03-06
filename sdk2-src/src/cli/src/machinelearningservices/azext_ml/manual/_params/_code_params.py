# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

from azure.cli.core.commands.parameters import get_three_state_flag
from ._common_params import add_common_params


def load_code_params(self):
    with self.argument_context("ml code create") as c:
        add_common_params(c)
        c.argument("name", options_list=["--name", "-n"], type=str, help="The name of the code asset.")
        c.argument("directory", help="The local path to the code.")
        c.argument("version", options_list=["--version", "-v"], help="The version of the code asset.")
        c.argument("datastore_name", help="The datastore to upload the artifact to.")
        c.argument("show_progress", arg_type=get_three_state_flag(), help="Show progress bar during upload.")

    with self.argument_context("ml code show") as c:
        add_common_params(c)
        c.argument("name", options_list=["--name", "-n"], type=str, help="The name of the code asset.")
