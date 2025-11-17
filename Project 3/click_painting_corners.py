"""
Interactive script to collect 4 corner points for all 6 painting images.

This script will:
1. Display each image one by one
2. Allow you to click 4 corner points on each painting
3. Save all corner points to 'painting_corners.npz'

Click the corners in this order for each image:
  1. Top-left corner
  2. Top-right corner
  3. Bottom-right corner
  4. Bottom-left corner

Usage:
    python click_painting_corners.py
"""

import numpy as np
import matplotlib.pyplot as plt
import os

# Painting dimensions (width, height) in centimeters
# Column 0 → width in centimeters
# Column 1 → height in centimeters
paintings_wh = np.array([
    [121.3,  82.9],   # Christina's World — Wyeth
    [ 92.1,  73.7],   # The Starry Night — Van Gogh
    [233.7, 243.9],   # Les Demoiselles d'Avignon — Picasso
    [390.1, 259.7],   # Dance (I) — Matisse
    [130.2, 162.3],   # Girl Before a Mirror — Picasso
    [200.7, 250.8],   # The Birth of the World — Miró
])

# Image file names
image_files = [
    'Christinas World — Wyeth.jpeg',
    'The Starry Night — Van Gogh.jpeg',
    'Les Demoiselles dAvignon — Picasso.jpeg',
    'Dance (I) — Matisse.jpeg',
    'Girl Before a Mirror — Picasso.jpeg',
    'The Birth of the World — Miró.jpeg'
]


def click_corners(image_path, title="Click 4 corners"):
    """
    Display an image and collect 4 corner points by clicking.
    
    Click in this order:
    1. Top-left corner
    2. Top-right corner
    3. Bottom-right corner
    4. Bottom-left corner
    
    Parameters:
    -----------
    image_path : str
        Path to the image file
    title : str
        Title to display on the window
    
    Returns:
    --------
    corners : numpy array of shape (4, 2)
        Corner points in order: [top-left, top-right, bottom-right, bottom-left]
    """
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image not found: {image_path}")
    
    img = plt.imread(image_path)
    
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.imshow(img)
    ax.set_title(title, fontsize=16, fontweight='bold')
    ax.axis('off')
    
    print("\n" + "="*70)
    print(title)
    print("="*70)
    print("Click 4 corners of the painting in this order:")
    print("  1. Top-left corner")
    print("  2. Top-right corner")
    print("  3. Bottom-right corner")
    print("  4. Bottom-left corner")
    print("Press ENTER when done")
    print("="*70)
    
    points = plt.ginput(n=4, timeout=0, show_clicks=True)
    plt.close(fig)
    
    corners = np.array(points)
    print(f"✓ Collected 4 corners from {image_path}")
    return corners


def main():
    """Main function to collect corner points for all 6 paintings."""
    
    print("\n" + "="*70)
    print("PAINTING CORNER POINT COLLECTION")
    print("="*70)
    print("\nThis script will help you click 4 corner points on each of the 6 painting images.")
    print("\nFor each image, click the corners in this order:")
    print("  1. Top-left corner of the painting")
    print("  2. Top-right corner of the painting")
    print("  3. Bottom-right corner of the painting")
    print("  4. Bottom-left corner of the painting")
    print("\n" + "="*70)
    
    # Check if corner points already exist
    if os.path.exists('painting_corners.npz'):
        response = input("\n⚠ 'painting_corners.npz' already exists. Overwrite? (y/n): ")
        if response.lower() != 'y':
            print("Exiting without overwriting.")
            return
    
    # Store corner points for each image
    corner_points = {}
    
    # Process each image
    for i, img_file in enumerate(image_files):
        width_cm, height_cm = paintings_wh[i]
        
        print(f"\n{'='*70}")
        print(f"Image {i+1}/6: {img_file}")
        print(f"Painting dimensions: {width_cm:.1f}cm × {height_cm:.1f}cm")
        print(f"Aspect ratio: {width_cm/height_cm:.3f}")
        print(f"{'='*70}")
        
        input(f"\nPress Enter to start clicking points on {img_file}...")
        
        # Click corners
        title = f"Image {i+1} - {img_file}\nClick 4 corners (Top-left, Top-right, Bottom-right, Bottom-left)"
        corners = click_corners(img_file, title)
        corner_points[i] = corners
        
        # Display collected points
        print(f"\nCollected points for Image {i+1}:")
        labels = ['Top-left', 'Top-right', 'Bottom-right', 'Bottom-left']
        for j, (label, point) in enumerate(zip(labels, corners)):
            print(f"  {label}: ({point[0]:.2f}, {point[1]:.2f})")
    
    # Save all corner points to file
    output_file = 'painting_corners.npz'
    np.savez(output_file,
             corners_0=corner_points[0],
             corners_1=corner_points[1],
             corners_2=corner_points[2],
             corners_3=corner_points[3],
             corners_4=corner_points[4],
             corners_5=corner_points[5])
    
    # Display summary
    print("\n" + "="*70)
    print("ALL CORNER POINTS COLLECTED SUCCESSFULLY!")
    print("="*70)
    print(f"\nPoints saved to: {output_file}")
    print("\nSummary:")
    for i in range(6):
        print(f"  Image {i+1} ({image_files[i]}): {len(corner_points[i])} points")
    
    print("\n" + "="*70)
    print("To load these points in your notebook, use:")
    print("  data = np.load('painting_corners.npz')")
    print("  corner_points = {")
    print("      0: data['corners_0'],")
    print("      1: data['corners_1'],")
    print("      2: data['corners_2'],")
    print("      3: data['corners_3'],")
    print("      4: data['corners_4'],")
    print("      5: data['corners_5']")
    print("  }")
    print("="*70)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠ Interrupted by user. Exiting...")
    except Exception as e:
        print(f"\n\n❌ Error: {e}")
        raise

