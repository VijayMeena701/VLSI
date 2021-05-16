`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date:    12:49:24 10/07/2020 
// Design Name: 
// Module Name:    paritygen 
// Project Name: 
// Target Devices: 
// Tool versions: 
// Description: 
//
// Dependencies: 
//
// Revision: 
// Revision 0.01 - File Created
// Additional Comments: 
//
//////////////////////////////////////////////////////////////////////////////////
module paritygen(
    input [7:0] a,
    output parity
    );
assign parity=a[7]^a[6]^a[5]^a[4]^a[3]^a[2]^a[1]^a[0];

endmodule
