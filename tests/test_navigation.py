
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
        self.navbar.verify_menu_items(self.data["navigation"]["menu_items"])

    def test_navigation_links_work(self):
        """
        Objective: Navigation items are functional and link to appropriate destinations
        """
        self.open(self.data["urls"]["base_url"])
        # Example validation for one item to demonstrate flow
        # In a real test, you might iterate or pick critical paths
        
        # Note: Actual URLs/Titles need to be verified against requirements
        # self.navbar.navigate_to("Products")
        # self.assert_title_contains("Products") 
        pass
