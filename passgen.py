#!/usr/bin/python
# encoding: utf-8

import sys
import argparse
from workflow import Workflow


log = None


def main(wf):
    if len(wf.args):
        query = wf.args[0]
    else:
        query = None
    # The Workflow instance will be passed to the function
    # you call from `Workflow.run`

    # Your imports here if you want to catch import errors
    from random import Random

    # args = parser.parse_args()
    rng = Random()

    # Variables and Args
    lefthand = '23456qwertasdfgzxcv'
    righthand = "789yuiophjknmb"
    allchars = righthand + lefthand
    alt_hands = True
    choices = ['alt', 'right', 'hand']
    passwordLength = 8

    args = wf.args

    log.debug(len(args))
    if len(args) == 0:
        arglist = [choices[0], passwordLength]
    elif len(args) == 1:
        arglist = query.split(' ')
        passwordLength = 8
        log.debug(arglist)
    elif len(args) == 2:
        arglist = query.split(' ')

    try:
        if arglist[0] in choices:
            pass
        else:
            log.debug("Default hand choice: %s" % choices[0])
            arglist[0] == "alt"
    except Exception, e:
        raise e
    try:
        if arglist[1]:
            passwordLength = int(arglist[1])
        else:
            passwordLength = 8
    except IndexError, e:
        passwordLength = 8
        log.debug("Using default password length: %s" % passwordLength)

    log.info('Password Length: %s' % passwordLength)
    if not arglist:
        arglist = ['alt', '8']

    try:
        #log.debug("Beginning try. Arglist: %s" % arglist)
        if len(arglist) >= 1:
            if arglist[0] == "alt":
                alt_hands = True
                try:
                    for i in range(6):
                        query = [rng.choice(allchars) for _ in range(passwordLength)]
                        query = ''.join(query)
                        wf.add_item(
                            title = ">  %s" % query,
                            subtitle = "Enter to copy to clipboard",
                            arg = query,
                            valid = True
                            )
                except Exception, e:
                    log.debug("Join range didn't work.")

            elif arglist[0] == "left":
                try:
                    for i in range(6):
                        query = [rng.choice(lefthand) for _ in range(passwordLength)]
                        query = ''.join(query)
                        wf.add_item(
                            title = ">  %s" % query,
                            subtitle = "Enter to copy to clipboard",
                            arg = query,
                            valid = True
                            )
                except Exception, e:
                    log.debug("Join range didn't work.")

            elif arglist[0] == "right":
                try:
                    for i in range(6):
                        query = [rng.choice(righthand) for _ in range(passwordLength)]
                        query = ''.join(query)
                        log.debug(query)
                        wf.add_item(
                            title = ">  %s" % query,
                            subtitle = "Enter to copy to clipboard",
                            arg = query,
                            valid = True
                            )
                except Exception, e:
                    log.debug("Join range didn't work.")

            else:
                log.debug("Wrong input: %s" % arglist)
                wf.add_item(
                    title = "Wrong input.",
                    subtitle = "Usage: pwd left 12  -  (Left hand, 12 chars)",
                    )
            log.debug("Generating wf.add_item. Options: {0} hand, {1} chars".format(arglist[0], arglist[1]))
        else:
            log.debug("Final else hit.")
            wf.add_item(
                title = "Something happened",
                subtitle = "We didn't generate anything."
            )
    except:
        log.debug("Could not parse args:")
        log.debug(arglist)

    wf.send_feedback()


if __name__ == '__main__':
    wf = Workflow()
    # Assign Workflow logger to a global variable, so all module
    # functions can access it without having to pass the Workflow
    # instance around
    log = wf.logger
    sys.exit(wf.run(main))
