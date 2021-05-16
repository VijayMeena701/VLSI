module pp(a,b,p);
input [31:0] a,b;
output [0:31][63:0] p;
reg [0:31][63:0] p;
integer i;
always@(*)
for(i=0;i<32;i=i+1)
begin
    p[i]=0;
    if (b[i]==1)
        p[i]=a;
    else
        p[i]=0;
    p[i]=p[i]<<i;
end
endmodule 