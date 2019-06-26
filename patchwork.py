#!/usr/bin/env python
from optparse import OptionParser
import logging

def main():
  usage = "usage: %prog [options]"
  parser = OptionParser(usage=usage)

  parser.add_option("-l", "--level", dest="loglevel", help="Set log level to LOGLEVEL", default="INFO")

  (options, _) = parser.parse_args()

  numeric_level = getattr(logging, options.loglevel.upper())
  if not isinstance(numeric_level, int):
    raise ValueError('Invalid log level: %s' % options.loglevel)

  logging.basicConfig(level=numeric_level)

if __name__ == "__main__":
  main()