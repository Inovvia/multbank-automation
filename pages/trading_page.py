from pages.base_page import BasePage


class TradingPage(BasePage):
    """
    Page Object for the Spot Trading functionality.
    """
    # Selectors
    MIN_TS_SEARCH = 3  # Minimum characters to search for trading pairs

    # Order Book Selectors
    ORDER_BOOK_TAB = "#ob"
    TRADES_TAB = "#trades"
    ORDER_BOOK_PANEL = "[role='tabpanel'][data-headlessui-state='selected']"
    
    # Asks (sell orders) and Bids (buy orders) containers
    # Desktop version uses ob-table-data, mobile uses mobile-ob-data
    # We target desktop by requiring ob-table-data in the class
    ASKS_CONTAINER = "[class*='ob-table-data'][class*='asks']"
    BIDS_CONTAINER = "[class*='ob-table-data'][class*='bids']"
    
    # Row selector using data-index attribute (stable, not affected by CSS hashing)
    ORDER_BOOK_ROW = "[data-index]"


    def open_order_book(self):
        self.click(self.ORDER_BOOK_TAB)

    def open_trades(self):
        self.click(self.TRADES_TAB)

    def get_trading_pairs(self):
        """
        Scrapes the trading pairs from the table.
        Returns a list of dictionaries or strings.
        """
        # Placeholder
        return []

    def verify_pair_present(self, pair_name):
        """Verifies that a specific pair is visible in the list."""
        pass

    def verify_order_book_and_trades_visible(self):
        """Verifies that the Order Book and Trades are visible."""
        self.open_order_book()
        self.assert_element(self.ORDER_BOOK_TAB)
        self.open_trades()
        self.assert_element(self.TRADES_TAB)

    def is_asks_visible(self):
        """Check if the asks (sell orders) container is visible."""
        return self.sb.is_element_visible(self.ASKS_CONTAINER)

    def is_bids_visible(self):
        """Check if the bids (buy orders) container is visible."""
        return self.sb.is_element_visible(self.BIDS_CONTAINER)

    def get_asks(self, limit=5):
        """Returns the top 'limit' ask orders (sell) if visible."""
        # Ensure we're on the Order Book tab
        self.open_order_book()
        self.sb.wait_for_element(self.ASKS_CONTAINER, timeout=10)
        if not self.is_asks_visible():
            return []
        return self._get_orders_from_container(self.ASKS_CONTAINER, limit=limit)

    def get_bids(self, limit=5):
        """Returns the top 'limit' bid orders (buy) if visible."""
        # Ensure we're on the Order Book tab
        self.open_order_book()
        self.sb.wait_for_element(self.BIDS_CONTAINER, timeout=10)
        if not self.is_bids_visible():
            return []
        return self._get_orders_from_container(self.BIDS_CONTAINER, limit=limit)


    def _get_orders_from_container(self, container_selector, limit):
        """Helper to extract orders from a specific container by selector."""
        try:
            container = self.sb.find_element(container_selector)
            rows = container.find_elements("css selector", self.ORDER_BOOK_ROW)
            
            orders = []
            for row in rows[:limit]:
                # Use XPath to get direct child divs 
                # Structure: div[0]=Price, div[1]=Size, div[2]=Total, div[3]=Bar(ignore)
                cells = row.find_elements("xpath", "./div")
                if len(cells) >= 3:  # Price, Size, Total
                    order = {
                        "price": cells[0].text.strip(),
                        "size": cells[1].text.strip(),
                        "total": cells[2].text.strip()
                    }
                    orders.append(order)
            return orders
        except Exception as e:
            print(f"Error extracting orders from {container_selector}: {e}")
            return []
