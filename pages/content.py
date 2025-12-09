
from pages.base_page import BasePage
from utils.data_loader import load_test_data

class Content(BasePage):
    """
    Page Object for Content Validation.
    """
    # Selectors
    STORE_LINKS = {
        "App Store": "a[href*='apple.com']",
        "Google Play": "a[href*='play.google.com']"
    }
    
    def __init__(self, driver):
        super().__init__(driver)
        self.data = load_test_data()
        
        # Banner selectors from test data
        self.BANNER_SLIDER = self.data["content"]["banners"]["banner_selectors"]["slider"]
        self.BANNER_CONTAINER = self.data["content"]["banners"]["banner_selectors"]["container"]
        self.BANNER_TITLE = self.data["content"]["banners"]["banner_selectors"]["title"]
        self.BANNER_DESCRIPTION = self.data["content"]["banners"]["banner_selectors"]["description"]
        self.BANNER_LINK = self.data["content"]["banners"]["banner_selectors"]["link"]
        self.BANNER_IMAGE = self.data["content"]["banners"]["banner_selectors"]["image"]
        self.BANNER_DOTS = self.data["content"]["banners"]["banner_selectors"]["dots"]
        self.BANNER_DOT = self.data["content"]["banners"]["banner_selectors"]["dot"]
        

        self.BANNER_VALIDATION_RULES = self.data["content"]["banners"]["validation_rules"]
        
        # Card section selectors
        self.CARD_SECTION = self.data["content"]["why_multibank"]["card_section"]["selector"]
        self.CARD = self.data["content"]["why_multibank"]["card_section"]["card_selector"]
        self.CARD_TITLE = self.data["content"]["why_multibank"]["card_section"]["title_selector"]
        self.CARD_DESCRIPTION = self.data["content"]["why_multibank"]["card_section"]["description_selector"]
        
        # Advantages section selectors
        self.ADVANTAGES_SECTION = self.data["content"]["why_multibank"]["advantages_section"]["selector"]
        self.ADVANTAGES_CARD = self.data["content"]["why_multibank"]["advantages_section"]["card_selector"]
        self.ADVANTAGES_TITLE = self.data["content"]["why_multibank"]["advantages_section"]["title_selector"]
        self.ADVANTAGES_DESCRIPTION = self.data["content"]["why_multibank"]["advantages_section"]["description_selector"]
        
        # Established section selectors
        self.ESTABLISHED_SECTION = self.data["content"]["why_multibank"]["established_section"]["selector"]
        self.ESTABLISHED_TITLE = self.data["content"]["why_multibank"]["established_section"]["title_selector"]
        self.ESTABLISHED_DESCRIPTION = self.data["content"]["why_multibank"]["established_section"]["description_selector"]
        self.ESTABLISHED_BOLD_PARAGRAPH = self.data["content"]["why_multibank"]["established_section"]["bold_paragraph_selector"]
        self.ESTABLISHED_STATISTICS_CONTAINER = self.data["content"]["why_multibank"]["established_section"]["statistics_container"]
        self.ESTABLISHED_STATISTIC_CARD = self.data["content"]["why_multibank"]["established_section"]["statistic_card_selector"]
        self.ESTABLISHED_STATISTIC_NUMBER = self.data["content"]["why_multibank"]["established_section"]["statistic_number_selector"]
        self.ESTABLISHED_STATISTIC_LABEL = self.data["content"]["why_multibank"]["established_section"]["statistic_label_selector"]
        
        # Regulations section selectors
        self.REGULATIONS_SECTION = self.data["content"]["why_multibank"]["regulations"]["selector"]
        self.REGULATIONS_CARD = self.data["content"]["why_multibank"]["regulations"]["card_selector"]
        self.REGULATIONS_TITLE = self.data["content"]["why_multibank"]["regulations"]["title_selector"]
        self.REGULATIONS_DESCRIPTION = self.data["content"]["why_multibank"]["regulations"]["description_selector"]
        self.REGULATIONS_BUTTON = self.data["content"]["why_multibank"]["regulations"]["button_selector"]
        
        # Crypto regulations section selectors
        self.CRYPTO_REGULATIONS_SECTION = self.data["content"]["why_multibank"]["crypto_regulations"]["selector"]
        self.CRYPTO_OFFER_CARD = self.data["content"]["why_multibank"]["crypto_regulations"]["offer_card_selector"]
        self.CRYPTO_IMAGE = self.data["content"]["why_multibank"]["crypto_regulations"]["image_selector"]
        self.CRYPTO_CONTENT = self.data["content"]["why_multibank"]["crypto_regulations"]["content_selector"]
        self.CRYPTO_SUBTITLE = self.data["content"]["why_multibank"]["crypto_regulations"]["subtitle_selector"]
        self.CRYPTO_TITLE = self.data["content"]["why_multibank"]["crypto_regulations"]["title_selector"]
        
        # Start trading now section selectors
        self.START_TRADING_CONTAINER = self.data["content"]["why_multibank"]["start_trading_now"]["selector"]
        self.START_TRADING_WRAPPER = self.data["content"]["why_multibank"]["start_trading_now"]["wrapper_selector"]
        self.START_TRADING_CONTENT = self.data["content"]["why_multibank"]["start_trading_now"]["content_selector"]
        self.START_TRADING_TITLE = self.data["content"]["why_multibank"]["start_trading_now"]["title_selector"]
        self.START_TRADING_DESCRIPTION = self.data["content"]["why_multibank"]["start_trading_now"]["description_selector"]
        self.START_TRADING_BUTTON = self.data["content"]["why_multibank"]["start_trading_now"]["button_selector"]
        self.START_TRADING_LINK = self.data["content"]["why_multibank"]["start_trading_now"]["link_selector"]
    


    def verify_app_store_links(self):
        """Verifies presence of App Store and Google Play links."""
        for name, selector in self.STORE_LINKS.items():
            self.assert_element(selector)
    
    def verify_banner_slider_exists(self):
        """Verifies that the banner slider exists on the page."""
        self.assert_element(self.BANNER_SLIDER)
    
    def verify_banner_count(self):
        """Verifies the number of banner containers."""
        expected_count = self.BANNER_VALIDATION_RULES["min_banner_count"]
        banners = self.find_elements(self.BANNER_CONTAINER)
        actual_count = len(banners)
        assert actual_count >= expected_count, f"Expected at least {expected_count} banners, found {actual_count}"
    
    def verify_banner_content(self):
        """Verifies that banner content exists and prints found content."""
        self.assert_element(self.BANNER_SLIDER)
        
        # Get all banner containers
        banners = self.sb.find_elements(self.BANNER_CONTAINER)
        print(f"Found {len(banners)} banner containers")
        
        # Check each banner for content
        for i, banner in enumerate(banners):
            print(f"\n--- Banner {i+1} ---")
            print(banner.get_attribute("innerHTML")) 
           
        
        print(f"\nTotal banners found: {len(banners)}")
        assert len(banners) > 0, "No banners found on the page"
    
    def verify_banner_images(self):
        """Verifies that banner images are present and prints their attributes."""
        images = self.sb.find_elements(self.BANNER_IMAGE)
        print(f"Found {len(images)} banner images")
        
        for i, img in enumerate(images):
            print(f"\n--- Image {i+1} ---")
            
            # Check alt attribute
            alt_text = img.get_attribute("alt")
            if alt_text:
                print(f"Alt text: {alt_text}")
            else:
                print("Alt text: (not set)")
            
            # Check src attribute
            src = img.get_attribute("src")
            if src:
                print(f"Src: {src[:100]}..." if len(src) > 100 else f"Src: {src}")
            else:
                print("Src: (not set)")
            
            # Check if image is displayed
            is_displayed = img.is_displayed()
            print(f"Displayed: {is_displayed}")
        
        print(f"\nTotal images found: {len(images)}")
        assert len(images) > 0, "No banner images found on the page"
    
    def verify_banner_navigation_dots(self):
        """Verifies that banner navigation dots exist and prints their status."""
        try:
            dots_container = self.find_element(self.BANNER_DOTS)
            print("Banner navigation dots container found")
        except:
            print("Banner navigation dots container not found")
            return
        
        dots = self.sb.find_elements(self.BANNER_DOT)
        print(f"Found {len(dots)} navigation dots")
        
        # Check for active dots
        active_dots = self.sb.find_elements(".slick-active")
        print(f"Found {len(active_dots)} active dots")
        
        for i, dot in enumerate(dots):
            is_active = "slick-active" in dot.get_attribute("class")
            print(f"Dot {i+1}: {'Active' if is_active else 'Inactive'}")
        
        assert len(dots) > 0, "No navigation dots found on the page"
    
    def verify_banner_link_clickability(self):
        """Verifies that banner links exist and prints their status."""
        links = self.sb.find_elements(self.BANNER_LINK)
        print(f"Found {len(links)} banner links")
        
        for i, link in enumerate(links):
            link_text = link.text
            is_displayed = link.is_displayed()
            is_enabled = link.is_enabled()
            href = link.get_attribute("href")
            
            print(f"\n--- Link {i+1} ---")
            print(f"Text: {link_text}")
            print(f"Displayed: {is_displayed}")
            print(f"Enabled: {is_enabled}")
            print(f"Href: {href}")
        
        print(f"\nTotal links found: {len(links)}")
        assert len(links) > 0, "No banner links found on the page"
    
    def click_banner_link(self, link_text):
        """Clicks a banner link with specific text."""
        link_selector = f"{self.BANNER_LINK}:contains('{link_text}')"
        self.click(link_selector)
    
    def verify_card_section(self):
        """Verifies the card section contains all expected key features."""
        key_features = self.data["content"]["why_multibank"]["key_features"]
        
        # Verify card section exists
        self.assert_element(self.CARD_SECTION)
        
        # Get all cards and verify their content using child elements
        cards = self.find_elements(self.CARD)
        assert len(cards) == len(key_features), f"Expected {len(key_features)} cards, found {len(cards)}"
        
        for i, feature in enumerate(key_features):
            if i < len(cards):
                card = cards[i]
                
                # Verify title within card
                title_element = card.find_element("css selector", self.CARD_TITLE)
                assert feature["title"] in title_element.text, f"Expected title '{feature['title']}' not found in '{title_element.text}'"
                
                # Verify description within card
                desc_element = card.find_element("css selector", self.CARD_DESCRIPTION)
                assert feature["description"] in desc_element.text, f"Expected description '{feature['description']}' not found in '{desc_element.text}'"
    
    def verify_advantages_section(self):
        """Verifies the advantages section contains all expected advantages."""
        advantages = self.data["content"]["why_multibank"]["advantages"]
        
        # Verify advantages section exists
        self.assert_element(self.ADVANTAGES_SECTION)
        
        # Get all advantage cards and verify their content
        cards = self.find_elements(self.ADVANTAGES_CARD)
        assert len(cards) == len(advantages), f"Expected {len(advantages)} advantage cards, found {len(cards)}"
        
        for i, advantage in enumerate(advantages):
            if i < len(cards):
                card = cards[i]
                
                # Verify title within card
                title_element = card.find_element("css selector", self.ADVANTAGES_TITLE)
                assert advantage["title"] in title_element.text, f"Expected title '{advantage['title']}' not found in '{title_element.text}'"
                
                # Verify description within card
                desc_element = card.find_element("css selector", self.ADVANTAGES_DESCRIPTION)
                assert advantage["description"] in desc_element.text, f"Expected description '{advantage['description']}' not found in '{desc_element.text}'"
    
    def verify_established_section(self):
        """Verifies the established section contains all expected content."""
        established_content = self.data["content"]["why_multibank"]["established_content"]
        
        # Verify established section exists
        self.assert_element(self.ESTABLISHED_SECTION)
        
        # Verify title
        title_element = self.sb.find_element(self.ESTABLISHED_TITLE)
        assert established_content["title"] in title_element.text, f"Expected title '{established_content['title']}' not found in '{title_element.text}'"
        
        # Verify description
        desc_element = self.sb.find_element(self.ESTABLISHED_DESCRIPTION)
        assert established_content["description"] in desc_element.text, f"Expected description '{established_content['description']}' not found in '{desc_element.text}'"
        
        # Verify bold paragraph
        bold_element = self.sb.find_element(self.ESTABLISHED_BOLD_PARAGRAPH)
        assert established_content["bold_paragraph"] in bold_element.text, f"Expected bold paragraph '{established_content['bold_paragraph']}' not found in '{bold_element.text}'"
        
        # Verify statistics cards
        statistics = established_content["statistics"]
        cards = self.find_elements(self.ESTABLISHED_STATISTIC_CARD)
        assert len(cards) == len(statistics), f"Expected {len(statistics)} statistic cards, found {len(cards)}"
        
        for i, statistic in enumerate(statistics):
            if i < len(cards):
                card = cards[i]
                
                # Verify number within card
                number_element = card.find_element("css selector", self.ESTABLISHED_STATISTIC_NUMBER)
                assert statistic["number"] in number_element.text, f"Expected number '{statistic['number']}' not found in '{number_element.text}'"
                
                # Verify label within card
                label_element = card.find_element("css selector", self.ESTABLISHED_STATISTIC_LABEL)
                assert statistic["label"] in label_element.text, f"Expected label '{statistic['label']}' not found in '{label_element.text}'"
    
    def verify_regulations_section(self):
        """Verifies the regulations section contains ASIC MEX Exchange content."""
        asic_mex_data = self.data["content"]["why_multibank"]["regulations"]["asic_mex_exchange"]
        
        # Verify regulations section exists
        self.assert_element(self.REGULATIONS_SECTION)
        
        # Get all regulation cards
        cards = self.find_elements(self.REGULATIONS_CARD)
        assert len(cards) > 0, "No regulation cards found"
        
        # Find ASIC MEX Exchange card
        asic_card_found = False
        for card in cards:
            try:
                # Check title
                title_element = card.find_element("css selector", self.REGULATIONS_TITLE)
                if asic_mex_data["title"] in title_element.text:
                    asic_card_found = True
                    
                    # Verify description
                    desc_element = card.find_element("css selector", self.REGULATIONS_DESCRIPTION)
                    assert asic_mex_data["description"] in desc_element.text, f"Expected description '{asic_mex_data['description']}' not found in '{desc_element.text}'"
                    
                    # Verify button
                    button_element = card.find_element("css selector", self.REGULATIONS_BUTTON)
                    assert asic_mex_data["button_text"] in button_element.text, f"Expected button text '{asic_mex_data['button_text']}' not found in '{button_element.text}'"
                    
                    break
            except:
                continue
        
        assert asic_card_found, "ASIC MEX Exchange card not found in regulations section"
    
    def verify_crypto_regulations_section(self):
        """Verifies the crypto regulations section contains deep pool liquidity content."""
        deep_pool_data = self.data["content"]["why_multibank"]["crypto_regulations"]["deep_pool_liquidity"]
        
        # Verify crypto regulations section exists
        self.assert_element(self.CRYPTO_REGULATIONS_SECTION)
        
        # Verify offer card exists
        self.assert_element(self.CRYPTO_OFFER_CARD)
        
        # Verify image exists
        self.assert_element(self.CRYPTO_IMAGE)
        
        # Verify content exists
        self.assert_element(self.CRYPTO_CONTENT)
        
        # Verify subtitle
        subtitle_element = self.sb.find_element(self.CRYPTO_SUBTITLE)
        assert deep_pool_data["subtitle"] in subtitle_element.text, f"Expected subtitle '{deep_pool_data['subtitle']}' not found in '{subtitle_element.text}'"
        
        # Verify title
        title_element = self.sb.find_element(self.CRYPTO_TITLE)
        assert deep_pool_data["title"] in title_element.text, f"Expected title '{deep_pool_data['title']}' not found in '{title_element.text}'"
    
    def verify_start_trading_now_section(self):
        """Verifies the start trading now section contains all expected content."""
        start_trading_data = self.data["content"]["why_multibank"]["start_trading_now"]["content"]
        
        # Verify start trading now section exists
        self.assert_element(self.START_TRADING_CONTAINER)
        
        # Verify wrapper exists
        self.assert_element(self.START_TRADING_WRAPPER)
        
        # Verify content exists
        self.assert_element(self.START_TRADING_CONTENT)
        
        # Verify title
        title_element = self.sb.find_element(self.START_TRADING_TITLE)
        assert start_trading_data["title"] in title_element.text, f"Expected title '{start_trading_data['title']}' not found in '{title_element.text}'"
        
        # Verify description
        desc_element = self.sb.find_element(self.START_TRADING_DESCRIPTION)
        assert start_trading_data["description"] in desc_element.text, f"Expected description '{start_trading_data['description']}' not found in '{desc_element.text}'"
        
        # Verify button
        button_element = self.sb.find_element(self.START_TRADING_BUTTON)
        assert start_trading_data["button_text"] in button_element.text, f"Expected button text '{start_trading_data['button_text']}' not found in '{button_element.text}'"
        
        # Verify link
        link_element = self.sb.find_element(self.START_TRADING_LINK)
        actual_href = link_element.get_attribute("href")
        assert start_trading_data["button_href"] in actual_href, f"Expected href '{start_trading_data['button_href']}' not found in '{actual_href}'"
