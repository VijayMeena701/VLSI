module Fulladder(a, b, c, s);
input [63:0] a, b;
input [64:0] c;
output reg [63:0] s;
//reg [63:0] s;
integer i;

always@(*)
begin
	for(i=0;i<64;i=i+1)
	begin
		s[i] = a[i] ^ b[i] ^ c[i];
	end
end

endmodule
