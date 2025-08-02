# test_pulsecore.py
"""
Tests for PulseCore module.
"""

import unittest
from pulsecore import PulseCore

class TestPulseCore(unittest.TestCase):
    """Test cases for PulseCore class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PulseCore()
        self.assertIsInstance(instance, PulseCore)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PulseCore()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
