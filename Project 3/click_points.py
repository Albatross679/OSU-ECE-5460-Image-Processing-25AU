"""
Interactive point clicking script for image correspondence.
This script allows you to click corresponding points on two images.

Usage:
    python click_points.py

The script will:
1. Display image_3.png and let you click points
2. Display image_4.png and let you click corresponding points
3. Save the points to 'correspondence_points.npz' file
"""

import numpy as np
import matplotlib.pyplot as plt
import os

def click_points_on_image(image_path, title, min_points=4):
    """
    Display an image and collect points by clicking.
    
    Parameters:
    -----------
    image_path : str
        Path to the image file
    title : str
        Title to display on the window
    min_points : int
        Minimum number of points required
    
    Returns:
    --------
    points : list of tuples
        List of (x, y) coordinates
    """
    # Load image
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image not found: {image_path}")
    
    img = plt.imread(image_path)
    
    # Display image
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.imshow(img)
    ax.set_title(title, fontsize=16, fontweight='bold')
    ax.axis('off')
    
    # Instructions
    print("\n" + "="*70)
    print(title)
    print("="*70)
    print(f"Instructions:")
    print(f"  - Left-click to select points (at least {min_points} points)")
    print(f"  - Points will be marked with red crosses as you click")
    print(f"  - Press ENTER when you're done selecting points")
    print(f"  - Right-click to remove the last point")
    print("="*70)
    
    # Collect points
    points = plt.ginput(n=-1, timeout=0, show_clicks=True)
    
    # Validate minimum points
    if len(points) < min_points:
        raise ValueError(f"Need at least {min_points} points, but only got {len(points)}")
    
    plt.close(fig)
    
    print(f"\n✓ Collected {len(points)} points from {image_path}")
    return points


def main():
    """Main function to click points on both images."""
    
    # Image paths
    img1_path = 'image_3.png'
    img2_path = 'image_4.png'
    
    print("\n" + "="*70)
    print("IMAGE CORRESPONDENCE POINT CLICKING")
    print("="*70)
    print("\nThis script will help you select corresponding points on two images.")
    print("You'll click points on Image 3 first, then corresponding points on Image 4.")
    print("\nIMPORTANT:")
    print("  - Click at least 4 points (more is better for accuracy)")
    print("  - Click corresponding points in the SAME ORDER on both images")
    print("  - Example: if you click the top-left corner first on Image 3,")
    print("    click the top-left corner first on Image 4 too")
    print("="*70)
    
    input("\nPress Enter to start clicking points on Image 3...")
    
    # Get points from first image
    points_img1 = click_points_on_image(
        img1_path, 
        'Image 3 - Click points (Press Enter when done)',
        min_points=4
    )
    
    print(f"\nYou clicked {len(points_img1)} points on Image 3.")
    print("\nNow you'll click the corresponding points on Image 4.")
    print("Make sure to click them in the SAME ORDER!")
    
    input(f"\nPress Enter to start clicking {len(points_img1)} points on Image 4...")
    
    # Get corresponding points from second image
    points_img2 = click_points_on_image(
        img2_path,
        f'Image 4 - Click {len(points_img1)} corresponding points in same order (Press Enter when done)',
        min_points=len(points_img1)
    )
    
    # Ensure same number of points
    if len(points_img2) != len(points_img1):
        print(f"\n⚠ Warning: Number of points don't match!")
        print(f"  Image 3: {len(points_img1)} points")
        print(f"  Image 4: {len(points_img2)} points")
        print(f"\nUsing first {min(len(points_img1), len(points_img2))} points from each image.")
        n_points = min(len(points_img1), len(points_img2))
        points_img1 = points_img1[:n_points]
        points_img2 = points_img2[:n_points]
    
    # Convert to numpy arrays
    image1points = np.array(points_img1)
    image2points = np.array(points_img2)
    
    # Save points to file
    output_file = 'correspondence_points.npz'
    np.savez(output_file, 
             image1points=image1points, 
             image2points=image2points)
    
    # Display results
    print("\n" + "="*70)
    print("POINTS COLLECTED SUCCESSFULLY!")
    print("="*70)
    print(f"\nTotal correspondences: {len(image1points)}")
    print(f"\nPoints saved to: {output_file}")
    print("\nImage 3 points:")
    for i, (x, y) in enumerate(image1points, 1):
        print(f"  Point {i}: ({x:.2f}, {y:.2f})")
    
    print("\nImage 4 points:")
    for i, (x, y) in enumerate(image2points, 1):
        print(f"  Point {i}: ({x:.2f}, {y:.2f})")
    
    print("\n" + "="*70)
    print("To use these points in your notebook, run:")
    print("  data = np.load('correspondence_points.npz')")
    print("  image1points = data['image1points']")
    print("  image2points = data['image2points']")
    print("="*70)
    
    # Also print as arrays for easy copying
    print("\nAs numpy arrays (for copying into notebook):")
    print("\nimage1points = np.array(")
    print(repr(image1points))
    print(")")
    print("\nimage2points = np.array(")
    print(repr(image2points))
    print(")")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠ Interrupted by user. Exiting...")
    except Exception as e:
        print(f"\n\n❌ Error: {e}")
        raise

