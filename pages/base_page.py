
class BasePage:
    """
    Base Page class that all other pages should inherit from.
    Provides common methods and wrapper around SeleniumBase functionality.
    """
    def __init__(self, sb):
        """
        :param sb: The SeleniumBase BaseCase instance (self).
        """
        self.sb = sb

    def open(self, url):
        """Navigates to the given URL."""
        self.sb.open(url)

    def click(self, selector, timeout=None):
        """Wrapper for sb.click with optional custom logging or error handling."""
        self.sb.click(selector, timeout=timeout)

    def type(self, selector, text, timeout=None):
        """Wrapper for sb.type."""
        self.sb.type(selector, text, timeout=timeout)

    def get_text(self, selector, timeout=None):
        """Wrapper for sb.get_text."""
        return self.sb.get_text(selector, timeout=timeout)

    def is_element_visible(self, selector, timeout=None):
        """Wrapper for sb.is_element_visible."""
        return self.sb.is_element_visible(selector, timeout=timeout)

    def assert_element(self, selector, timeout=None):
        """Wrapper for sb.assert_element."""
        self.sb.assert_element(selector, timeout=timeout)
    
    def assert_text(self, text, selector="html", timeout=None):
        """Wrapper for sb.assert_text."""
        self.sb.assert_text(text, selector, timeout=timeout)

    def hover(self, selector, timeout=None):
        """Wrapper for sb.hover."""
        self.sb.hover(selector, timeout=timeout)
