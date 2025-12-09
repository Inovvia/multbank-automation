
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

    def test_categories(self):
        """
        Objective: Verify that the categories section displays correctly
        """
        primary_pair = self.data["trading"]["primary_pair"]
        self.open(self.data["urls"]["base_url"] + "trade/" + primary_pair)
        
        # Get categories from test data
        categories = self.data["trading"]["categories"]
        assert len(categories) > 0, "No categories defined in test data"

        self.trading_page.open_categories()        
        # Use JavaScript to interact with the search input directly
        # This bypasses visibility issues

        
        for category in categories:
            category_text = self.trading_page.select_category(category)
            print(f"\nSelected category '{category}': {category_text}")
            
            
            # Get trading pairs data from the table
            pairs_data = self.trading_page.get_trading_pairs_data(limit=5)
            
            # Verify we got some pairs
            assert len(pairs_data) > 0, f"No trading pairs found for category: {category}"
            print(f"  Found {len(pairs_data)} trading pairs")
            
            # Verify structure of each pair
            for pair in pairs_data:
                self.trading_page.verify_trading_pair_structure(pair)
                print(f"  [OK] {pair['pair']}: Price={pair['price']}, Change={pair['change']}% ({pair['changeDirection']})")

