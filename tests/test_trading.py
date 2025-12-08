
from seleniumbase import BaseCase
from pages.trading_page import TradingPage
from utils.data_loader import load_test_data

class TestTrading(BaseCase):
    def setUp(self):
        super().setUp()
        self.data = load_test_data()
        self.trading_page = TradingPage(self)

    def test_order_book_functionality(self):
        """
        Objective: Verify that the Order Book section displays correctly and contains valid data.
        """
        # Use primary pair for testing
        primary_pair = self.data["trading"]["primary_pair"]
        pair_url = self.data["urls"]["base_url"] + "trade/" + primary_pair
        
        self.open(pair_url)
        
        # Verify Order Book is visible
        self.trading_page.verify_order_book_and_trades_visible()
        
        # Verify Asks
        asks = self.trading_page.get_asks(limit=5)
        assert len(asks) > 0, "No ask orders found in the Order Book"
        print(f"Top Ask: {asks[0]}")
        
        # Verify Bids
        bids = self.trading_page.get_bids(limit=5)
        assert len(bids) > 0, "No bid orders found in the Order Book"
        print(f"Top Bid: {bids[0]}")
        
        # Verify Structure Fields (Price, Size)
        required_fields = ["price", "size"]
        for order in asks + bids:
            for field in required_fields:
                assert field in order, f"Order missing field: {field}"
                assert order[field] != "", f"Order field {field} is empty"

    def test_chart_visibility(self):
        """
        Objective: Verify that the chart section displays correctly
        """
        primary_pair = self.data["trading"]["primary_pair"]
        self.open(self.data["urls"]["base_url"] + "trade/" + primary_pair)
        #TODO: Add chart visibility verification


