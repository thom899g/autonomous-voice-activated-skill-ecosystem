from typing import Dict, Any
import logging

class SmartHomeController:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        
    def control_device(self, device_id: str, action: str) -> bool:
        """Controls smart home devices via voice commands."""
        try:
            # Mock device control logic
            self.logger.info(f"Controlling device {device_id}: {action}")
            return True
        except Exception as e:
            self.logger.error(f"Device control failed: {str(e)}")
            raise

    def get_device_status(self, device_id: str) -> Dict[str, Any]:
        """Retrieves status of a smart home device."""
        try:
            # Mock status retrieval
            status = {"status": "on", "last_update": "now"}
            self.logger.info(f"Retrieved status for device {device_id}")
            return status
        except Exception as e:
            self.logger.error(f"Status retrieval failed: {str(e)}")
            raise