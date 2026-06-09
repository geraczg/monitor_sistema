import unittest

from src.monitor import parse_args, validate_limits


class MonitorCliTests(unittest.TestCase):
    def test_parse_once_and_custom_limits(self) -> None:
        args = parse_args(["--once", "--warning", "75", "--critical", "95"])

        self.assertTrue(args.once)
        self.assertEqual(args.warning, 75.0)
        self.assertEqual(args.critical, 95.0)

    def test_validate_limits_rejects_invalid_order(self) -> None:
        with self.assertRaises(ValueError):
            validate_limits(90.0, 80.0)


if __name__ == "__main__":
    unittest.main()
