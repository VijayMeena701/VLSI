module FullAdder(s, cout, a, b, cin);
input a, b, cin;
output s, cout;
wire w0,w1,w2,w3,w4;

xor xor_0(w0, a, b);
xor xor_1(s, w0, cin);
and and_0(w1, a, b);
and and_1(w2, b, cin);
and and_2(w3, cin, a);
or or_0(w4, w1, w2);
or or_1(cout, w4, w3);

endmodule

module level(s, cout, c, d, cin);
input [15:0] c, d;
input cin;
output [15:0] s;
output cout;
wire [14:0] ca;

FullAdder FA_0(s[0], ca[0], d[1], c[0], 1'b0);
FullAdder FA_1(s[1], ca[1], d[2], c[1], ca[0]);
FullAdder FA_2(s[2], ca[2], d[3], c[2], ca[1]);
FullAdder FA_3(s[3], ca[3], d[4], c[3], ca[2]);
FullAdder FA_4(s[4], ca[4], d[5], c[4], ca[3]);
FullAdder FA_5(s[5], ca[5], d[6], c[5], ca[4]);
FullAdder FA_6(s[6], ca[6], d[7], c[6], ca[5]);
FullAdder FA_7(s[7], ca[7], d[8], c[7], ca[6]);
FullAdder FA_8(s[8], ca[8], d[9], c[8], ca[7]);
FullAdder FA_9(s[9], ca[9], d[10], c[9], ca[8]);
FullAdder FA_10(s[10], ca[10], d[11], c[10], ca[9]);
FullAdder FA_11(s[11], ca[11], d[12], c[11], ca[10]);
FullAdder FA_12(s[12], ca[12], d[13], c[12], ca[11]);
FullAdder FA_13(s[13], ca[13], d[14], c[13], ca[12]);
FullAdder FA_14(s[14], ca[14], d[15], c[14], ca[13]);
FullAdder FA_15(s[15], cout, c[15], ca[14], cin);

endmodule


module ArrayMultiplier(p, a, b);
input [15:0] a, b;
output [31:0] p;
reg [15:0] ai[15:0];
reg [15:0] c;
integer i, j;

always@(*)
begin
    for(i=0;i<16;i=i+1)
    begin
        for(j=0;j<16;j=j+1)
        begin
            c[j] = b[i] & a[j];
        end
        ai[i] = c;
    end
end


assign p[0] = a[0] & b[0];

wire [15:0] s1;
wire cout1;
level l_0(s1, cout1, ai[1], ai[0], 1'b0);
assign p[1] = s1[0];

wire [15:0] s2;
wire cout2;
level l_1(s2, cout2, ai[2], s1, cout1);
assign p[2] = s2[0];

wire [15:0] s3;
wire cout3;
level l_2(s3, cout3, ai[3], s2, cout2);
assign p[3] = s3[0];

wire [15:0] s4;
wire cout4;
level l_3(s4, cout4, ai[4], s3, cout3);
assign p[4] = s4[0];

wire [15:0] s5;
wire cout5;
level l_4(s5, cout5, ai[5], s4, cout4);
assign p[5] = s5[0];

wire [15:0] s6;
wire cout6;
level l_5(s6, cout6, ai[6], s5, cout5);
assign p[6] = s6[0];

wire [15:0] s7;
wire cout7;
level l_6(s7, cout7, ai[7], s6, cout6);
assign p[7] = s7[0];

wire [15:0] s8;
wire cout8;
level l_7(s8, cout8, ai[8], s7, cout7);
assign p[8] = s8[0];

wire [15:0] s9;
wire cout9;
level l_8(s9, cout9, ai[9], s8, cout8);
assign p[9] = s9[0];

wire [15:0] s10;
wire cout10;
level l_9(s10, cout10, ai[10], s9, cout9);
assign p[10] = s10[0];

wire [15:0] s11;
wire cout11;
level l_10(s11, cout11, ai[11], s10, cout10);
assign p[11] = s10[0];

wire [15:0] s12;
wire cout12;
level l_11(s12, cout12, ai[12], s11, cout11);
assign p[12] = s12[0];

wire [15:0] s13;
wire cout13;
level l_12(s13, cout13, ai[13], s12, cout12);
assign p[13] = s13[0];

wire [15:0] s14;
wire cout14;
level l_13(s14, cout14, ai[14], s13, cout13);
assign p[14] = s14[0];

wire [15:0] s15;
wire cout15;
level l_14(s15, cout15, ai[15], s14, cout14);
assign p[30:15] = s15;
assign p[31] = cout15;

endmodule