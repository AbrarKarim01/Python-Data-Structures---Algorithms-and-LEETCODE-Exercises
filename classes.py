class Cookie:
    def __init__(self, color): # constructor_color(self):
        """Returns the color of the cookie."""
        self.color = color

    def get_color(self):
        """Returns the color of the cookie."""
        return self.color
    
    def set_color(self, color):
        """Sets the color of the cookie."""
        self.color = color

Cookie_one = Cookie("green") # constructor_color(self):
Cookie_two = Cookie("blue")

print("Cookie one is", Cookie_one.get_color())  # Output: green
print("Cookie two is", Cookie_two.get_color())  # Output: blue

Cookie_one.set_color("red")
print("Cookie one is now", Cookie_one.get_color())  # Output: red
print("Cookie two is still", Cookie_two.get_color())  # Output: blue