#!/usr/bin/env python
from optparse import OptionParser
import logging

def main():
  usage = "usage: %prog [options]"
  parser = OptionParser(usage=usage)

  parser.add_option("-l", "--level", dest="loglevel", help="Set log level to LOGLEVEL", default="INFO")

  (options, _) = parser.parse_args()

  configureLogging(options.loglevel.upper())
  logger = logging.getLogger(__name__)

  logger.info("Starting run")

  # TODO Add the fun bits here.

  logger.info("Complete")

def configureLogging(level):
  numeric_level = getattr(logging, level)
  if not isinstance(numeric_level, int):
    raise ValueError('Invalid log level: %s' % level)

  logger = logging.getLogger()
  logger.setLevel(numeric_level)

  # Use stdout/stderr
  ch = logging.StreamHandler()

  formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
  ch.setFormatter(formatter)

  logger.addHandler(ch)

if __name__ == "__main__":
  main()
