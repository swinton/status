#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os, json

import requests


def handler(event, context):
    response = requests.get(event["url"])
    message = "All is well" if response.ok else "Site may be down, better investigate ASAP"

    return dict(url=event["url"], status_code=response.status_code, ok=response.ok, message=message)


if __name__ == "__main__":
    # Read event, context from sys.argv
    args = [json.loads(arg) for arg in sys.argv[1:2]]

    # Provide None for event, context if not provided
    while len(args) < 2:
        args.append(None)

    # Print the output
    print json.dumps(handler(*args), indent=4)
