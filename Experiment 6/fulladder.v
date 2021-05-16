module fulladder(a, b, c, s);
input [31:0] a, b;
input [32:0] c;
output reg [31:0] s;
//reg [31:0] s;
integer i;

always@(*)
begin
	for(i=0;i<32;i=i+1)
	begin
		s[i] = a[i] ^ b[i] ^ c[i];
	end
end

endmodule
