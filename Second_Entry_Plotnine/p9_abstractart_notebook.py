# -*- coding: utf-8 -*-
"""p9_AbstractArt_notebook.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1379LYaa4j5B5G1eVK79cb6COTQoY1Xjx

# 🎨 Contest Submission: Abstract Art with plotnine (Entry 2)
> "Art enables us to find ourselves and lose ourselves at the same time."

# 🎯 Motivation
This submission is a tribute to the versatility and artistic potential of the ```plotnine``` package, inspired by its foundation in the ggplot2 package from R, which is heavily used in the R community. The idea for this plot arose from a desire to create something unique and visually striking, pushing the boundaries of traditional data visualization into the realm of digital art. After viewing other submissions and exploring Python and R graph galleries, I decided to create a series of artistic plots using plotnine, with guidance and inspiration from my brother and leveraging AI chatbots to speed up the iterative process. 🎨✨

## 📦 Package Requirements
"""

pip install -q plotnine pandas numpy

"""> "Where words fail, art speaks." 🎨

## ✨ Features Highlighted
1. ```geom_point()```: Used to create individual points in the plot, adding variety with the size and color aesthetics.
2. ```geom_path()```: For creating continuous lines and paths, like spirals and geometric shapes.
3. ```geom_density_2d()```: Adds density contours to highlight data concentration areas.
4. ```geom_text()```: Used to add annotations, such as letters around the central circular plot.
5. ```theme_dark()``` and ```theme_minimal()```: Showcase the customization capabilities of plotnine themes to create aesthetically pleasing backgrounds and remove unnecessary plot elements.
6. ```scale_color_brewer()``` and ```scale_color_gradient()```: Demonstrates color scaling to enhance visual appeal and distinguish plot elements.
7. ```coord_fixed()```: Ensures equal scaling of the x and y axes for accurate representation of circular and square elements.
8. ```labs()```: Adds informative titles to the plots.

## 📜 Documentation and Processing Steps
1. **Data Generation**: Each plot starts with generating or transforming data to fit the desired artistic concept. This includes creating random data points, generating spirals, or calculating geometric shapes.
2. **Aesthetic Mapping**: Using plotnine's aes function to map data variables to visual properties such as position, color, and size.
3. **Layering**: Adding multiple layers to the plots, including points, paths, density contours, and text annotations, to build up the final visual.
4. **Theming**: Applying plot themes and adjusting plot background, axis elements, and grid lines to enhance the visual style.
5. **Scaling**: Using color and size scales to improve the distinction between different plot elements.
6. **Saving**: Saving the plots as high-resolution images for submission and further use.

## Plot 1: Abstract Art with plotnine
* "Inspired by abstract expressionism, this plot aims to blend random data points with geometric paths to create a visually intriguing piece."
"""

import pandas as pd
import numpy as np
from plotnine import *
import random

# Create some data
n = 1000
df = pd.DataFrame({
    'x': np.random.uniform(-10, 10, n),
    'y': np.random.uniform(-10, 10, n),
    'group': np.random.choice(['A', 'B', 'C', 'D'], n),
    'size': np.random.uniform(1, 5, n)
})

# Create some spiral data
t = np.linspace(0, 4*np.pi, 200)
spiral_df = pd.DataFrame({
    'x': t * np.cos(t),
    'y': t * np.sin(t)
})

# Create the plot
plot = (
    ggplot()
    + geom_point(df, aes(x='x', y='y', color='group', size='size'), alpha=0.6)
    + geom_path(spiral_df, aes(x='x', y='y'), color='white', size=1, alpha=0.5)
    + geom_density_2d(df, aes(x='x', y='y'), color='yellow', alpha=0.2)
    + scale_color_brewer(type='qual', palette='Set1')
    + theme_dark()
    + theme(
        plot_background=element_rect(fill='black'),
        panel_background=element_rect(fill='black'),
        legend_position='none',
        axis_title=element_blank(),
        axis_text=element_blank(),
        axis_ticks=element_blank(),
        panel_grid=element_blank()
    )
    + labs(title='Abstract Art with plotnine')
    + xlim(-12, 12)
    + ylim(-12, 12)
)

print(plot)

# Save the plot
plot.save('abstract_art_plotnine.png', dpi=300)
print("Plot saved as 'abstract_art_plotnine.png'")

"""## Plot 2: Vitruvian Data Visualization
* "This plot pays homage to Da Vinci's Vitruvian Man, integrating geometric shapes and golden ratio spirals to explore the harmony of art and science."
"""

import pandas as pd
import numpy as np
from plotnine import *
import string

# Generate data for the main circular plot
n = 1000
t = np.linspace(0, 2*np.pi, n)
r = 1 + 0.3 * np.sin(5*t) + 0.1 * np.cos(10*t)
x = r * np.cos(t)
y = r * np.sin(t)

df = pd.DataFrame({
    'x': x,
    'y': y,
    't': t,
    'r': r,
    'group': np.repeat(range(10), 100)
})

# Create additional geometric elements
circle_df = pd.DataFrame({'t': np.linspace(0, 2*np.pi, 100)})
circle_df['x'] = np.cos(circle_df['t'])
circle_df['y'] = np.sin(circle_df['t'])

square_df = pd.DataFrame({
    'x': [-1, -1, 1, 1, -1],
    'y': [-1, 1, 1, -1, -1]
})

# Create golden ratio spiral
golden_ratio = (1 + 5**0.5) / 2
theta = np.linspace(0, 4*np.pi, 1000)
a = 0.1
golden_spiral_df = pd.DataFrame({
    'x': a * np.exp(theta / golden_ratio) * np.cos(theta),
    'y': a * np.exp(theta / golden_ratio) * np.sin(theta)
})

# Generate text points
text_points = []
for i, letter in enumerate(string.ascii_uppercase):
    angle = i * 2 * np.pi / 26
    x = 1.2 * np.cos(angle)
    y = 1.2 * np.sin(angle)
    text_points.append((x, y, letter))

text_df = pd.DataFrame(text_points, columns=['x', 'y', 'letter'])

# Create the enhanced plot
plot = (
    ggplot()
    + geom_path(circle_df, aes(x='x', y='y'), color='goldenrod', size=1, alpha=0.7)
    + geom_path(square_df, aes(x='x', y='y'), color='goldenrod', size=1, alpha=0.7)
    + geom_path(golden_spiral_df, aes(x='x', y='y'), color='blue', size=0.5, alpha=0.5)
    + geom_point(df, aes(x='x', y='y', color='r', size='r'), alpha=0.7)
    + geom_path(df, aes(x='x', y='y', group='group', color='r'), alpha=0.3)
    + geom_text(text_df, aes(x='x', y='y', label='letter'), color='darkgoldenrod', size=8, fontweight='bold')
    + geom_segment(aes(x=0, y=0, xend='x', yend='y'), data=text_df, color='goldenrod', alpha=0.3)
    + scale_color_gradient2(low='blue', mid='purple', high='red', midpoint=1)
    + scale_size_continuous(range=(0.5, 3))
    + coord_fixed(ratio=1)
    + theme_minimal()
    + theme(
        plot_title=element_text(face="bold", size=16, hjust=0.5),
        plot_background=element_rect(fill='#F0E68C'),
        panel_background=element_rect(fill='#F0E68C'),
        legend_position='none',
        axis_title=element_blank(),
        axis_text=element_blank(),
        axis_ticks=element_blank(),
        panel_grid=element_blank()
    )
    + labs(title='Vitruvian Data Visualization')
    + xlim(-1.5, 1.5)
    + ylim(-1.5, 1.5)
)

print(plot)
# ggsave(plot, filename='enhanced_vitruvian_plot.png', dpi=300)
plot.save('enhanced_vitruvian_plot.png', dpi=300)
print("Plot saved as 'enhanced_vitruvian_plot.png'")

"""## Plot 3: Floral Pattern 🌸
* "Designed to mimic the intricate beauty of floral patterns, this plot captures the elegance of natural forms using mathematical expressions."
"""

import pandas as pd
import numpy as np
from plotnine import *

# Create data for floral pattern
t = np.linspace(0, 2*np.pi, 1000)
df = pd.DataFrame({
    'x': np.cos(t) * (1 + 0.9 * np.cos(8*t)) * (1 + 0.1 * np.cos(24*t)),
    'y': np.sin(t) * (1 + 0.9 * np.cos(8*t)) * (1 + 0.1 * np.cos(24*t)),
    'color': np.sin(t)
})

# Create the plot
plot = (
    ggplot(df, aes(x='x', y='y', color='color'))
    + geom_path(size=1.5, alpha=0.8)
    + geom_point(size=0.5)
    + scale_color_gradient(low='purple', high='pink')
    + theme_void()
    + theme(
        plot_background=element_rect(fill='black'),
        legend_position='none'
    )
    + labs(title='Floral Pattern')
    + coord_fixed(ratio=1)
)

print(plot)

# Save the plot
plot.save('floral_pattern.png', dpi=300)
print("Plot saved as 'floral_pattern.png'")

"""## Plot 4: Geometric Abstract 🔺🔵◼️
* "A tribute to the simplicity and beauty of geometric shapes, this plot combines randomness with smooth trends to create a modern abstract piece."

"""

import pandas as pd
import numpy as np
from plotnine import *

# Create data for various shapes
n = 1000
df = pd.DataFrame({
    'x': np.random.uniform(0, 10, n),
    'y': np.random.uniform(0, 10, n),
    'size': np.random.uniform(1, 5, n),
    'shape': np.random.choice(['circle', 'square', 'triangle'], n)
})

# Create the plot
plot = (
    ggplot(df, aes(x='x', y='y', size='size', shape='shape'))
    + geom_point(color='white', alpha=0.6)
    + geom_smooth(method='lm', se=False, color='red', size=1)
    + geom_rug(color='yellow', alpha=0.5, sides='bl')
    + scale_shape_manual(values=['o', 's', '^'])
    + theme_minimal()
    + theme(
        plot_title=element_text(face="bold", size=16, hjust=0.5, color = "white"),
        plot_background=element_rect(fill='navy'),
        panel_background=element_rect(fill='navy'),
        legend_position='none',
        axis_title=element_blank(),
        axis_text=element_blank(),
        axis_ticks=element_blank(),
        panel_grid=element_blank()
    )
    + labs(title='Geometric Abstract')
)

print(plot)

# Save the plot
plot.save('geometric_abstract.png', dpi=300)
print("Plot saved as 'geometric_abstract.png'")

"""## 🎨 Conclusion
These artistic plots aim to showcase the flexibility and power of plotnine in creating visually appealing and complex data visualizations. By blending traditional charting techniques with creative designs, these plots illustrate the potential for data visualization tools to venture beyond analysis and into the realm of art.
"""