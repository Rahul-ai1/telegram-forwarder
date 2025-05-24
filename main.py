#!/usr/bin/env python3
"""
Telegram Channel Message Forwarder (Main Entry Point)

This script sets up and runs the Telegram forwarder bot
with automatic restart capabilities for 24/7 operation.
"""

import os
import time
import logging
import subprocess
import sys

# Setup logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def run_bot():
    """Run the Telegram forwarder bot with automatic restart"""
    
    while True:
        try:
            logger.info("Starting Telegram forwarder bot process...")
            
            # Start the bot as a subprocess
            process = subprocess.Popen([sys.executable, "telegram_forwarder.py"])
            
            # Wait for the process to terminate
            exit_code = process.wait()
            
            # Check exit code and decide to restart
            if exit_code != 0:
                logger.warning(f"Bot process exited with code {exit_code}. Restarting in 10 seconds...")
                time.sleep(10)
            else:
                logger.info("Bot process terminated normally. Restarting in 5 seconds...")
                time.sleep(5)
                
        except KeyboardInterrupt:
            logger.info("Received shutdown signal. Stopping bot...")
            break
        except Exception as e:
            logger.error(f"Error running bot: {e}", exc_info=True)
            logger.info("Waiting 30 seconds before restarting...")
            time.sleep(30)

if __name__ == "__main__":
    logger.info("Starting 24/7 Telegram forwarder bot monitor...")
    run_bot()