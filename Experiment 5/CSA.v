module CSA (a,b,c,sum,car);
input [63:0] a,b,c;
output reg [63:0] sum,car;
integer i;
always@(*)
    for(i=0;i<64;i=i+1)
    begin
    car[0]=0;
    sum[i] = a[i]^b[i]^c[i];
    car[i+1] = ( a[i] & b[i] ) | ( b[i] & c[i] ) | ( c[i] & a[i] );
    end
endmodule
