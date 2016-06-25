# Copyright (C) Check Point Software Technologies LTD.
# This file is part of Cuckoo Sandbox - http://www.cuckoosandbox.org
# See the file 'docs/LICENSE' for copying permission.

from lib.cuckoo.common.abstracts import Signature

class AndroidStopProcess(Signature):
    name = "application_stopped_processes"
    description = "Application Stopped Processes (Dynamic)"
    severity = 2
    categories = ["android"]
    authors = ["idanr1986"]
    minimum = "0.5"

    def run(self):
        try:
            if "killed_process" in self.results["droidmon"]:
                return True
            else:
                return False
        except:
            return False
