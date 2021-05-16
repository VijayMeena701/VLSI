module kpg(a, b, cout);
input [31:0] a, b;
output reg [31:0] [1:0] cout;
integer i;

always@(*)
for(i=0;i<32;i=i+1)
begin
if(a[i] == 0)
begin
	if(b[i] == 0)
		cout[i] = 2'b00;
	else
		cout[i] = 2'b01;
end
else
begin
	if(b[i] == 1)
		cout[i] = 2'b11;
	else
		cout[i] = 2'b01;
end
end

endmodule
