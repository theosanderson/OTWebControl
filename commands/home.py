import opentrons.execute
import logging
logger = logging.Logger("log")
protocol = opentrons.execute.get_protocol_api('2.6')

def main():
    protocol.home()
    input("Protocol complete. Press enter to finish.")


try:
    main()
except Exception:
    logger.error("Fatal error:", exc_info=True)
    input("Press enter to return to the menu.")