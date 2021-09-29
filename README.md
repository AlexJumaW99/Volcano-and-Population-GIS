# Volcano-and-Population-GIS
A program that marks the exact location of various Volcanoes on a map based on their coordinates (latitude and longitude), on one layer. On another layer it show the population of each country in the world.
Both layers can be shown one at a time, simultaneously, or not even shown at all - leaving a blank world map. This can be done using the layer controller, found on the top right of the page. 

The color of the volcano marker depends on the height of the volcano:

    1. Green - less than 2000m in height
    2. Orange - 2000 - 3000m
    3. Red - greater than 3000m
    
Clicking on a volcano marker provides additional info about the volcano, such as the name (which is clickable and redirects the user to a Google search result that gives additional info about the volcano clicked), and the elevation. 

NB: The OUTPUT can be found in the 'Map2.html' file.

# What I Learnt:
1. How to create a feature group with Folium, and add them as children to the map, in order to add various layers to the GIS.
2. How to use the iFrame object to add Html code to our Python doc. 
3. How to add GeoJson data that allows us to visualize the population ranges of each country in the world. 


