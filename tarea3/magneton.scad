$fn=100;
include <modules.scad>

magnemite();

translate([0,10,-14])
rotate([-120,0,0])
magnemite();

translate([0,-10,-14])
rotate([120,0,0])
magnemite();