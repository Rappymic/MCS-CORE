class Browser:
    def __init__(self, name, engine, developer):
        self.name = name
        self.engine = engine
        self.developer = developer

    def get_details(self):
        return f"{self.name} is developed by {self.developer} and uses {self.engine}"

firefox = Browser("Mozilla_Firefox", "Ghecko", "Mozilla Corporation")
chrome = Browser("Google Chrome", "Blink", "Google Corp.")
safari = Browser("Apple Safari", "Webkit", "Apple")

print(firefox.get_details())
print(chrome.get_details())
print(safari.get_details())