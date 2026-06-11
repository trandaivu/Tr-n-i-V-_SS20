import unittest
from btth import calculate_total_revenue


class TestRevenue(unittest.TestCase):

    def test_revenue_with_booked_and_cancelled(self):
        tickets = [
            {
                "ticket_id": "T01",
                "buyer_name": "A",
                "price": 500.0,
                "status": "Booked",
                "seat": ("A", 1)
            },
            {
                "ticket_id": "T02",
                "buyer_name": "B",
                "price": 300.0,
                "status": "Cancelled",
                "seat": ("B", 2)
            },
            {
                "ticket_id": "T03",
                "buyer_name": "C",
                "price": 700.0,
                "status": "Booked",
                "seat": ("C", 3)
            }
        ]

        self.assertEqual(
            calculate_total_revenue(tickets),
            1200.0
        )

    def test_revenue_empty_list(self):
        self.assertEqual(
            calculate_total_revenue([]),
            0.0
        )

if __name__ == "__main__":
    unittest.main()