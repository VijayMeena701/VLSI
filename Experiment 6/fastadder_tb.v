`include "kpg.v"
`include "ppc.v"
`include "fulladder.v"

module fastadder;
reg [31:0] a, b;
reg cin;
wire [31:0] [1:0] c;
wire [32:0] carry;
wire [31:0] s;

initial
begin
	a = 32'hC090F0D0;
	b = 32'hCF00FADB;
	cin = 1'b1;
	#10 cin = 1'b0;
end

kpg kpg_0(a, b, c);
ppc ppc_0(c, cin, carry);
fulladder adder_0(a, b, carry, s);

initial
	$monitor($time,"  A = %b;\n\t\t      B = %b;\n\t\t    Carryin = %b;\n\t\t    sum = %b;\n\t\t",a, b, cin, s);
	
endmodule
