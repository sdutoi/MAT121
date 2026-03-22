import numpy as np
import matplotlib.pyplot as plt

def plot_l3_ball():
    """
    Generates and saves the plot for the L3 unit ball: |x|^3 + |y|^3 = 1
    """
    
    # Create x values from -1 to 1
    x = np.linspace(-1, 1, 400)
    
    # Calculate |x|^3
    x_abs_cubed = np.abs(x)**3
    
    # Calculate |y| = (1 - |x|^3)^(1/3)
    y_abs = (1 - x_abs_cubed)**(1/3)
    
    # Create the plot
    plt.figure(figsize=(6, 6))
    
    # Plot the top half (y >= 0)
    plt.plot(x, y_abs, label=r'$|y| = (1 - |x|^3)^{1/3}$', color='blue')
    # Plot the bottom half (y < 0)
    plt.plot(x, -y_abs, color='blue')
    
    # Fill the unit ball
    plt.fill_between(x, y_abs, -y_abs, color='blue', alpha=0.3)
    
    # Formatting
    plt.title(r'Unit Ball for $L_3$ Norm ($||(x, y)||_3 \leq 1$)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.xlim(-1.2, 1.2)
    plt.ylim(-1.2, 1.2)
    
    # Save the plot
    plt.savefig('plot1.png')
    print("Saved 'plot1.png' (L3 unit ball)")
    plt.close()

def plot_heart_ball():
    """
    Generates and saves the plot for the 'heart' unit ball: x^2 + 2y^2 = 1
    """
    
    # Create x values from -1 to 1
    x = np.linspace(-1, 1, 400)
    
    # Solve for y: 2y^2 = 1 - x^2  =>  y = +/- sqrt((1 - x^2) / 2)
    # Use np.maximum to avoid sqrt of tiny negative numbers due to float precision
    y_squared = np.maximum(0, (1 - x**2) / 2)
    y_pos = np.sqrt(y_squared)
    
    # Create the plot
    plt.figure(figsize=(6, 6))
    
    # Plot the top half (y >= 0)
    plt.plot(x, y_pos, label=r'$y = \sqrt{(1 - x^2) / 2}$', color='red')
    # Plot the bottom half (y < 0)
    plt.plot(x, -y_pos, color='red')
    
    # Fill the unit ball
    plt.fill_between(x, y_pos, -y_pos, color='red', alpha=0.3)
    
    # Formatting
    plt.title(r'Unit Ball for $\heartsuit$ Norm ($||(x, y)||_{\heartsuit} \leq 1$)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.xlim(-1.2, 1.2)
    plt.ylim(-1.2, 1.2)

    # Save the plot
    plt.savefig('plot2.png')
    print("Saved 'plot2.png' (Heart unit ball)")
    plt.close()

if __name__ == '__main__':
    plot_l3_ball()
    plot_heart_ball()