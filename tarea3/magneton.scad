$fn=100;
include <modules.scad>

translate([0,0,7])
union(){
    eye();
    rotate([-55,0,0]) translate([0,14,0]) rotate([10,0,15]) eye();
    rotate([-125,0,0])translate([0,14,0]) rotate([10,0,15]) eye();
};


translate([-1,18, -1])
rotate([20,10,10])
magnet();

translate([-0,12, -14])
rotate([-70,-15,15])
magnet();


translate([-1,-18, -1])
rotate([160,10,-10])
rotate([0,180,0])
magnet();

translate([-0,-12, -14])
rotate([250,-15,-15])
rotate([0,180,0])
magnet();

translate([1,9.5, 12])
rotate([30,0,-10])
magnet();

translate([1,-9.5, 12])
rotate([150,0,10])
rotate([0,180,0])
magnet();

