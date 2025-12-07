
from seleniumbase import BaseCase
from pages.navigation_bar import NavigationBar
from utils.data_loader import load_test_data

class TestNavigation(BaseCase):
    def setUp(self):
        super().setUp()
        self.data = load_test_data()
        self.navbar = NavigationBar(self)

    def test_navigation_menu_displays_correctly(self):
        """
        Objective: Top navigation menu displays correctly with all expected options
        """
        self.open(self.data["urls"]["base_url"])
        self.navbar.verify_navbar_visible()
        menu_names = [item["name"] for item in self.data["navigation"]["menu_items"]]
        self.navbar.verify_menu_items(self.data["navigation"]["menu_items"])

    def test_dropdown_navigation(self):
        """
        Objective: Dropdown menus open and their links navigate correctly
        """
        base_url = self.data["urls"]["base_url"].rstrip("/")
        menu_items = self.data["navigation"]["menu_items"]

        for menu in menu_items:
            # Skip menus without dropdowns
            if not menu["dropdown"]:
                continue

            print(f"Testing dropdown: {menu['name']}")
            
            for item in menu["dropdown"]:
                self.open(self.data["urls"]["base_url"])
                
                self.wait_for_element_visible(menu["selector"])
                self.click(menu["selector"])
                
                item_name = item["name"]
                
                # Simplified selector logic that avoids complex XPaths which might break JS fallback
                # Use a specific strategy for "Spot" if needed, otherwise generic text
                if item_name == "Spot":
                    # Use exact text match to avoid matching "Spot Exchange"
                    # and check for both span and a tags by using *
                    item_selector = f"//*[normalize-space(text())='{item_name}']"
                else:
                    item_selector = f"//*[contains(text(), '{item_name}')]"

                self.wait_for_element_visible(item_selector)
                
                self.click(item_selector)
                expected_url = item["expected_url"]
                
                if expected_url.startswith("http"):
                    self.assert_url_contains(expected_url)
                elif expected_url == "/":
                    self.assert_url_contains(base_url)
                else:
                    self.assert_url_contains(expected_url)
                
                print(f"  [PASS] {item_name} -> {expected_url}")

    def test_navigation_links_work(self):
        """
        Objective: Navigation items are functional and link to appropriate destinations
        """
        base_url = self.data["urls"]["base_url"].rstrip("/")
        links = self.data["navigation"]["links"]
        
        for link in links:
            self.open(self.data["urls"]["base_url"])
            
            self.wait_for_element_visible(link["selector"], timeout=10)
            self.click(link["selector"])
            
            expected_url = link["expected_url"]
            if expected_url == "/":
                self.assert_url_contains(base_url)
            else:
                self.assert_url_contains(expected_url)
            
            print(f"[PASS] {link['name']} navigated to {expected_url}")
