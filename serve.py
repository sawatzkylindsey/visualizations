
from argparse import ArgumentParser
import logging
import os
import sys

from otter.handler import Echo
from otter.server import run_server
from pytils.log import setup_logging, teardown, user_log

from src import handler
from src import model


@teardown
def main(argv):
    ap = ArgumentParser(prog="serve")
    ap.add_argument("-v", "--verbose", default=False, action="store_true", help="Turn on verbose logging.")
    ap.add_argument("-p", "--port", default=8888, type=int)
    ap.add_argument("timeline_file")
    aargs = ap.parse_args(argv)
    setup_logging(".%s.log" % os.path.splitext(os.path.basename(__file__))[0], aargs.verbose, False, True, True)
    logging.debug(aargs)
    run_server(aargs.port, "api", "resources", {
        "event-timeline": handler.StaticJsonContent(aargs.timeline_file, lambda d: model.EventTimeline(d)),
    })
    return 0


if __name__ == "__main__":
    main(sys.argv[1:])

