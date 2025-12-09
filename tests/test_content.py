
from seleniumbase import BaseCase
from pages.content import Content
from utils.data_loader import load_test_data

class TestContent(BaseCase):
    def setUp(self):
        super().setUp()
        self.data = load_test_data()
        self.content = Content(self)


    def test_banner_slider_exists(self):
        """
        Objective: Banner slider exists on the page
        """
        self.open(self.data["urls"]["base_url"])
        self.content.verify_banner_slider_exists()

    def test_banner_count(self):
        """
        Objective: Correct number of banners are displayed
        """
        self.open(self.data["urls"]["base_url"])
        self.content.verify_banner_count()

    def test_banner_content(self):
        """
        Objective: All expected banner content is present
        """
        self.open(self.data["urls"]["base_url"])
        self.content.verify_banner_content()

    def test_banner_images(self):
        """
        Objective: Banner images are properly loaded with correct attributes
        """
        self.open(self.data["urls"]["base_url"])
        self.content.verify_banner_images()

    def test_banner_navigation_dots(self):
        """
        Objective: Banner navigation dots exist and are functional
        """
        self.open(self.data["urls"]["base_url"])
        self.content.verify_banner_navigation_dots()

    def test_banner_link_clickability(self):
        """
        Objective: Banner links are clickable and functional
        """
        self.open(self.data["urls"]["base_url"])
        self.content.verify_banner_link_clickability()

    def test_app_store_links(self):
        """
        Objective: Download section links correctly to App Store and Google Play
        """
        self.open(self.data["urls"]["base_url"])
        self.content.verify_app_store_links()

