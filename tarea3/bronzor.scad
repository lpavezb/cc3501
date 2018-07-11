$fn=50;
r=[0,90,0];

//main cylinder
color([0,128/255,128/255])
difference(){
    rotate(r) cylinder(h=1,r=10,center=true);
    rotate(r) cylinder(h=1.1,r=7,center=true);
}

//spheres
for(i=[0:5])
    rotate([60*i,0,0])
    translate([0,0,10])
        color([0,70/255,128/255])
        sphere(1.5);
color([0,70/255,128/255])

//center cylinders
difference() {
    rotate(r) cylinder(h=1.3,r=7,center=true);
    translate([1,0,0]) rotate(r) cylinder(h=1.3,r=4,center=true);
}

//face
translate([0.1,0,0]){
color([0,0,0])
difference(){
    rotate(r) cylinder(h=1.1,r=4,center=true);
    rotate(r) cylinder(h=1.2,r=3.9,center=true);
}
color([0,70/255,128/255])
rotate(r) cylinder(h=1.1,r=3.9,center=true);


//eyes
////right eye
r_e = [90,0,90];
s = 0.2;
s2 = 0.05;
color([1,1,1])
translate([0.5,3.4,0])
rotate(r_e) 
    scale([s*1.2,2*s,s]) cylinder(h=1,r=5, center=true);
color([0,0,0])
translate([0.6,3.4,0])
rotate(r_e) 
    scale([s2*1.5,4*s2,s2]) cylinder(h=1,r=5, center=true);

////left eye
color([1,1,1])
translate([0.5,-3.4,0])
rotate(r_e) 
    scale([s*1.2,2*s,s]) cylinder(h=1,r=5, center=true);
color([0,0,0])
translate([0.6,-3.4,0])
rotate(r_e) 
    scale([s2*1.5,4*s2,s2]) cylinder(h=1,r=5, center=true);

//center sphere
color([0,128/255,128/255])
translate([0.6,0,0])
intersection(){
    translate([4.5,0,0]) cube(10,center=true);
    sphere(1.5);
}

//mid ring spheres
color([0,128/255,128/255]){
rotate([55,0,0])
translate([0.3,4,0]) sphere(0.6);
rotate([125,0,0])
translate([0.3,4,0]) sphere(0.6);
rotate([-55,0,0])
translate([0.3,4,0]) sphere(0.6);
rotate([-125,0,0])
translate([0.3,4,0]) sphere(0.6);
}
}