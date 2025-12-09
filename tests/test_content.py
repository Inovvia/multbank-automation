
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

    def test_why_multibank_content(self):
        """
        Objective: About Us -> Why MultiBank page renders all expected components
        """
        self.open(self.data["urls"]["about_url"])
        
        # Check page title
        expected_title = self.data["content"]["why_multibank"]["page_title"]
        self.assert_title_contains(expected_title)
        
        # Check hero section
        hero_headline = self.data["content"]["why_multibank"]["hero_section"]["headline"]
        self.assert_text(hero_headline)
        
        hero_subheadline_selector = self.data["content"]["why_multibank"]["hero_section"]["subheadline_selector"]
        hero_subheadline_text = self.data["content"]["why_multibank"]["hero_section"]["subheadline"]
        self.assert_text(hero_subheadline_text, selector=hero_subheadline_selector)
                
        # Check card section key features
        self.content.verify_card_section()
        
        # Check advantages section
        self.content.verify_advantages_section()
        
        # Check established section
        self.content.verify_established_section()
        
        # Check regulations section
        self.content.verify_regulations_section()
        
        # Check crypto regulations section
        self.content.verify_crypto_regulations_section()
        
        # Check start trading now section
        self.content.verify_start_trading_now_section()
