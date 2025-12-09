from pages.base_page import BasePage



class TradingPage(BasePage):
    MIN_TS_SEARCH = 3
    ORDER_BOOK_TAB = "#ob"
    TRADES_TAB = "#trades"
    ORDER_BOOK_PANEL = "[role='tabpanel'][data-headlessui-state='selected']"
    ASKS_CONTAINER = "[class*='ob-table-data'][class*='asks']"
    BIDS_CONTAINER = "[class*='ob-table-data'][class*='bids']"
    ORDER_BOOK_ROW = "[data-index]"
    CATEGORIES_TAB = "#trade-pair"


    def open_order_book(self):
        self.click(self.ORDER_BOOK_TAB)

    def open_trades(self):
        self.click(self.TRADES_TAB)
    
    def open_categories(self):
        self.click(self.CATEGORIES_TAB)

    def get_trading_pairs(self):
        return []

    def verify_pair_present(self, pair_name):
        pass

    def verify_order_book_and_trades_visible(self):
        self.open_order_book()
        self.assert_element(self.ORDER_BOOK_TAB)
        self.open_trades()
        self.assert_element(self.TRADES_TAB)

    def is_asks_visible(self):
        return self.sb.is_element_visible(self.ASKS_CONTAINER)

    def is_bids_visible(self):
        return self.sb.is_element_visible(self.BIDS_CONTAINER)

    def get_asks(self, limit=5):
        self.open_order_book()
        self.sb.wait_for_element(self.ASKS_CONTAINER, timeout=10)
        if not self.is_asks_visible():
            return []
        return self._get_orders_from_container(self.ASKS_CONTAINER, limit=limit)

    def get_bids(self, limit=5):
        self.open_order_book()
        self.sb.wait_for_element(self.BIDS_CONTAINER, timeout=10)
        if not self.is_bids_visible():
            return []
        return self._get_orders_from_container(self.BIDS_CONTAINER, limit=limit)


    def _get_orders_from_container(self, container_selector, limit):
        try:
            container = self.sb.find_element(container_selector)
            rows = container.find_elements("css selector", self.ORDER_BOOK_ROW)
            
            orders = []
            for row in rows[:limit]:
                cells = row.find_elements("xpath", "./div")
                if len(cells) >= 3:
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

    def get_categories(self):
        return self.sb.get_text(self.CATEGORIES_TAB)
    
    def select_category(self, category):
        category_id = category.lower()
        
        select_script = f"""
        const categoryElement = document.getElementById('{category_id}');
        if (categoryElement) {{
            categoryElement.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
            categoryElement.style.display = 'block';
            categoryElement.style.visibility = 'visible';
            const elementText = categoryElement.textContent || categoryElement.innerText;
            categoryElement.click();
            return elementText.trim();
        }}
        return null;
        """
        
        result = self.sb.execute_script(select_script)
        if not result:
            raise Exception(f"Failed to select category: {category}")
        
        return result
    
    def get_trading_pairs_data(self, limit=None):
        extract_script = """
        const table = document.getElementById('trade-pairs');
        if (!table) return null;
        
        const rows = table.querySelectorAll('tbody tr[data-index]');
        const pairs = [];
        
        rows.forEach(row => {
            const dataIndex = row.getAttribute('data-index');
            const pairCell = row.querySelector('td[id$="_pair-td"]');
            const pairNameSpan = pairCell ? pairCell.querySelector('span[id^="pair-name-"]:not([id$="-favorite"])') : null;
            const pairName = pairNameSpan ? pairNameSpan.textContent.trim() : '';
            
            const priceTd = row.querySelector('td[id$="_price-td"]');
            const price = priceTd ? priceTd.textContent.trim() : '';
            
            const changeSpan = row.querySelector('span[id$="-24h-change"]');
            const change = changeSpan ? changeSpan.textContent.trim() : '';
            
            const changePill = row.querySelector('.style_pill__aksoI');
            let changeDirection = 'neutral';
            if (changePill) {
                if (changePill.classList.contains('style_positive__AMUJ7')) {
                    changeDirection = 'positive';
                } else if (changePill.classList.contains('style_negative__6FJgg')) {
                    changeDirection = 'negative';
                }
            }
            
            const icons = row.querySelectorAll('.style_icons__OBea5 img');
            const hasIcons = icons.length >= 2;
            
            pairs.push({
                index: parseInt(dataIndex),
                pair: pairName,
                price: price,
                change: change,
                changeDirection: changeDirection,
                hasIcons: hasIcons
            });
        });
        
        return pairs;
        """
        
        pairs = self.sb.execute_script(extract_script)
        
        if pairs is None:
            return []
        
        if limit is not None:
            pairs = pairs[:limit]
        
        return pairs
    
    def verify_trading_pair_structure(self, pair_data):
        required_fields = ['pair', 'price', 'change', 'changeDirection', 'hasIcons']
        
        for field in required_fields:
            if field not in pair_data:
                raise AssertionError(f"Missing required field: {field}")
            
            if field != 'hasIcons' and not pair_data[field]:
                raise AssertionError(f"Field '{field}' is empty for pair: {pair_data.get('pair', 'Unknown')}")
        
        if '-' not in pair_data['pair']:
            raise AssertionError(f"Invalid pair name format: {pair_data['pair']} (expected format: XXX-YYY)")
        
        price_clean = pair_data['price'].replace(',', '')
        try:
            float(price_clean)
        except ValueError:
            raise AssertionError(f"Invalid price format: {pair_data['price']} for pair: {pair_data['pair']}")
        
        try:
            float(pair_data['change'])
        except ValueError:
            raise AssertionError(f"Invalid change format: {pair_data['change']} for pair: {pair_data['pair']}")
        
        if pair_data['changeDirection'] not in ['positive', 'negative', 'neutral']:
            raise AssertionError(f"Invalid change direction: {pair_data['changeDirection']} for pair: {pair_data['pair']}")
        
        if not pair_data['hasIcons']:
            raise AssertionError(f"Missing icons for pair: {pair_data['pair']}")
        
        return True

