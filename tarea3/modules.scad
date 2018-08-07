module eye(){
    union(){
        color(1/255*[112,128,144])
        difference(){
            sphere(7);
            difference(){
                sphere(11);
                translate([-4,0,0]) cube(20, center=true);
            };
        };

        union(){
            color([1,1,1])
            sphere(6.95);
            color([0,0,0])
            translate([0.05,0,0])
            intersection(){
                sphere(7);
                rotate([0,90,0]) cylinder(r=0.6,h=10);
            };
        };
    };
}
module Ushape(ur1, ur2 ,uh) {

    // Circle resolution
    cRes = 30;
    // Extrusion resolution
    eRes = 50;

    union(){
        // The rounded part
        intersection(){
        rotate_extrude(convexity=10, $fn=eRes)
               translate([ur2, 0]) square(ur1, $fn=cRes);
        translate([0,7,0])cube(14, center = true);
        };
        
        // U extensions
        rotate([90,0,0]) linear_extrude(height=uh,$fn=eRes)
               translate([ur2, 0]) square(ur1, $fn=cRes);
        rotate([90,0,0]) linear_extrude(height=uh,$fn=eRes)
               translate([1.8*-ur2, 0]) square(ur1, $fn=cRes);
        
    }

}
module magnet(){
    scale(0.8)
    union(){
        color([0,0,0])
        translate([1,0])rotate([180,90,0]) Ushape(2.4,3,5);
        color([1,0,0])translate([-0.2,6.2,4.2])cube(2.4, center=true);
        color([0,0,1])translate([-0.2,6.2,-4.2])cube(2.4, center=true);
    };
};