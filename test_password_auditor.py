
import unittest
from password_auditor import audit_password


class TestPasswordAuditor(unittest.TestCase):

    def test_strong_password(self):
        checks = audit_password("Cyber@123")
        self.assertEqual(sum(checks.values()), 5)

    def test_short_password(self):
        checks = audit_password("Ab@1")
        self.assertFalse(checks["Minimum 8 characters"])

    def test_missing_number(self):
        checks = audit_password("Cyber@Pass")
        self.assertFalse(checks["Contains a number"])

    def test_missing_special_symbol(self):
        checks = audit_password("Cyber123")
        self.assertFalse(checks["Contains a special symbol"])


if __name__ == "__main__":
    unittest.main()
