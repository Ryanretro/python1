def lab_assesment_description():
    """This program demonstrates the changing of  the value of a variable. It needs to starts with the original value and then updates it."""
    # Original value
    product = "This is Samsung"
    # Display the original value
    print("Original Value:", product)
    # Change the value to "This is Apple"
    product = "This is Apple"
    # Display the updated value
    print("Updated Value:", product)
if __name__ == "__main__":
    lab_assesment_description()


import math
def calculate_cone_surface_area(radius, height):
    """Calculate the surface area of a cone.
    Args:
        radius (float): The radius of the base of the cone.
        height (float): The height of the cone.
    Returns:
        float: The surface area of the cone.
    """
    slant_height = math.sqrt(radius ** 2 + height ** 2)
    surface_area = math.pi * radius * (radius + slant_height)
    return surface_area
def calculate_cone_volume(radius, height):
    """Calculate the volume of a cone.
    Args:
        radius (float): The radius of the base of the cone.
        height (float): The height of the cone.
    Returns:
        float: The volume of the cone.
    """
    volume = (1/3) * math.pi * radius ** 2 * height
    return volume
# Input values
radius = float(input("Enter the radius of the cone: "))
height = float(input("Enter the height of the cone: "))
# Calculate and print the surface area and volume
surface_area = calculate_cone_surface_area(radius, height)
volume = calculate_cone_volume(radius, height)
print(f"The area of the cone is {surface_area:.2f}, and the volume is {volume:.2f}")