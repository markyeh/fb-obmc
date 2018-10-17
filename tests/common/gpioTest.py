from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import sys
import unitTestUtil
import logging
import os
import time

def read_data(path):
    handle = open(path, "r")
    data = handle.readline().rstrip()
    handle.close()
    logger.debug("reading path={} data={}".format(path, data))
    return data


def gpio_test(data):
    """
    given a json of gpios and expected values, check that all of the gpios
    exist and its values
    """
    for gpioname, v in data['gpios'].items():
        gpio_path = "/tmp/gpionames/" + str(gpioname)
        if not os.path.exists(gpio_path):
            print("GPIO test : Missing GPIO={} [FAILED]".format(gpioname))
            sys.exit(1)
        else:
            logger.debug("GPIO name={} present".format(gpioname))
            checker = [
                "active_low",
                "direction",
                "edge",
                "value"
            ]
            for item in checker:
                vpath = gpio_path + "/" + item
                rdata = read_data(vpath)
                jdata = v[item]
                if rdata not in jdata:
                    print("GPIO test : Incorrect {} for GPIO={} [FAILED]".format(item, gpioname))
                    sys.exit(1)
    print("GPIO test [PASSED]")
    sys.exit(0)

if __name__ == "__main__":
    """
    Input to this file should look like the following:
    python gpioTest.py gpiolist.json
    """
    util = unitTestUtil.UnitTestUtil()
    logger = util.logger(logging.WARN)
    try:
        data = {}
        args = util.Argparser(['json', '--verbose'], [str, None],
                              ['json file',
                              'output all steps from test with mode options: DEBUG, INFO, WARNING, ERROR'])
        if args.verbose is not None:
            logger = util.logger(args.verbose)
        data = util.JSONparser(args.json)
        gpio_test(data)
    except Exception as e:
        print("GPIO test [FAILED]")
        print("Error code returned: " + str(e))
    sys.exit(1)
