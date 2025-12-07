
from pages.base_page import BasePage

class NavigationBar(BasePage):
    """
    Page Object for the Top Navigation Menu.
    """
    NAV_CONTAINER = "#__next > div > header"

    def verify_navbar_visible(self):
        """Verifies that the navigation bar is displayed."""
        self.assert_element(self.NAV_CONTAINER)

    def verify_menu_items(self, expected_items):
        """
        Verifies that all expected menu items are present.
        If a menu item has a dropdown, it verifies the dropdown content as well.
        :param expected_items: list of dicts containing 'name', 'selector', and optional 'dropdown'.
        """
        for item in expected_items:
            # Verify the main menu item exists
            self.click(item["selector"])
            self.assert_element(item["selector"])
            
            # If there are dropdown items, verify them
            if "dropdown" in item and item["dropdown"]:
                # Hover to reveal the dropdown
                self.hover(item["selector"])
                
                for sub_item in item["dropdown"]:
                    self.assert_element(f"//*[contains(text(), '{sub_item}')]")
                

    def navigate_to(self, menu_name):
        """Clicks on a specific menu item."""
        selector = f"//nav//a[contains(text(), '{menu_name}')]"
        self.click(selector)
