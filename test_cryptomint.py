# test_cryptomint.py
"""
Tests for CryptoMint module.
"""

import unittest
from cryptomint import CryptoMint

class TestCryptoMint(unittest.TestCase):
    """Test cases for CryptoMint class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CryptoMint()
        self.assertIsInstance(instance, CryptoMint)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CryptoMint()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
