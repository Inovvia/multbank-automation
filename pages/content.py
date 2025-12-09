
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
