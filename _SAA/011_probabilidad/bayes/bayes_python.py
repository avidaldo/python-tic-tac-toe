import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# Create a Venn diagram
venn = plt.figure()
venn = plt.gca()

# Add circles that represent A and B
venn.add_patch(plt.Circle((0.4, 0.5), 0.2, color='blue', alpha=0.5))  # Circle A
venn.add_patch(plt.Circle((0.6, 0.5), 0.2, color='green', alpha=0.5))  # Circle B

# Add text labels for A, B, and A ∩ B
venn.text(0.35, 0.5, 'A', ha='center', va='center', fontsize=13)
venn.text(0.65, 0.5, 'B', ha='center', va='center', fontsize=13)
venn.text(0.5, 0.5, 'A ∩ B', ha='center', va='center', fontsize=12)

# Add a rectangle that represents Omega with padding
padding = 0.1  # Adjust as needed
omega = Rectangle((padding, padding), 1 - 2*padding, 1 - 2*padding, fill=None, alpha=1)
venn.add_patch(omega)

# Add Omega symbol in the corner of the rectangle with some margin
omega_padding = 0.02  # Adjust as needed
venn.text(padding + omega_padding, 1 - padding - omega_padding, 'Ω', ha='left', va='top', fontsize=18)

# Configure the aspect
venn.set_xlim(0, 1)
venn.set_ylim(0, 1)
venn.axis('off')  # Turn off the axes

plt.show()  # Show the diagram