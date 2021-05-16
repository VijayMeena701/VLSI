module ppc(c, cin, cout);
input [63:0] [1:0] c;
input cin;
output reg [64:0] cout;
reg [63:0] [1:0] w0,w1,w2,w3,w4,w5;
integer i,j,k;

always@(*)
begin
for(i=1;i<64;i=i+1)
begin
	w0[i] = c[i];
end

for(i=1;i<64;i=i*2)
begin
for(j=0;j<64;j=j+1)
begin
if(i+j < 64)
begin
if(w0[j+i] == 2'b01)
begin
if(w0[j] == 2'b00)
w0[j+i] = 2'b00;
else if(w0[j] == 2'b11)
w0[j+i] = 2'b11;
else
w0[j+i] = 2'b01;
end
end
end
end
end

always@(*)
begin
cout[0] = cin;
for(k=0;k<64;k=k+1)
begin
if(w0[k] == 2'b00)
cout[k+1] = 0;
else if(w0[k] == 2'b11)
cout[k+1] = 1;
else
cout[k+1] = cout[k];
end
end

endmodule
