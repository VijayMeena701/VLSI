`include "CSA.v"
`include "pp.v"
`include "kpg.v"
`include "ppc.v"
`include "Fulladder.v"

module tb;

//varables for carry save adder (CSA)
wire [1:30][63:0] sum,car;

//variables for fast adder 
reg cin;
wire [63:0] [1:0] c_add;
wire [64:0] carry;
wire [63:0] s;

//for partial product 
wire [0:31][63:0] p;
reg [31:0] e,f;
pp pp_1(e,f,p);

//carry save adder

CSA a1(p[0],p[1],p[2],sum[1],car[1]);
CSA a2(p[3],p[4],p[5],sum[2],car[2]);
CSA a3(p[6],p[7],p[8],sum[3],car[3]);
CSA a4(p[9],p[10],p[11],sum[4],car[4]);
CSA a5(p[12],p[13],p[14],sum[5],car[5]);
CSA a6(p[15],p[16],p[17],sum[6],car[6]);
CSA a7(p[18],p[19],p[20],sum[7],car[7]);
CSA a8(p[21],p[22],p[23],sum[8],car[8]);
CSA a9(p[24],p[25],p[26],sum[9],car[9]);
CSA a10(p[27],p[28],p[29],sum[10],car[10]);

CSA a11(sum[1],car[1],sum[2],sum[11],car[11]);
CSA a12(car[2],car[3],sum[3],sum[12],car[12]);
CSA a13(sum[4],car[4],sum[5],sum[13],car[13]);
CSA a14(sum[6],car[5],car[6],sum[14],car[14]);
CSA a15(sum[7],car[7],sum[8],sum[15],car[15]);
CSA a16(sum[9],car[8],car[9],sum[16],car[16]);
CSA a17(sum[10],car[10],p[30],sum[17],car[17]);

CSA a18(sum[11],car[11],sum[12],sum[18],car[18]);
CSA a19(sum[13],car[12],car[13],sum[19],car[19]);
CSA a20(sum[14],car[14],sum[15],sum[20],car[20]);
CSA a21(sum[16],car[15],car[16],sum[21],car[21]);
CSA a22(sum[17],car[17],p[31],sum[22],car[22]);

CSA a23(sum[18],car[18],sum[19],sum[23],car[23]);
CSA a24(sum[20],car[20],car[19],sum[24],car[24]);
CSA a25(sum[21],car[21],sum[22],sum[25],car[25]);

CSA a26(sum[24],car[23],sum[23],sum[26],car[26]);
CSA a27(sum[25],car[24],car[25],sum[27],car[27]);

CSA a28(sum[26],car[26],sum[27],sum[28],car[28]);

CSA a29(car[27],car[28],sum[28],sum[29],car[29]);

CSA a30(car[22],car[29],sum[29],sum[30],car[30]);
initial
begin
            e=32'd12;
            f=32'd21;
            cin=1'b0;
            #5 e=32'd256;
            #5 f=32'd8;
            #5 e=32'd25200;

end
 //for 64 bit fast adder addition 
kpg kpg_0(sum[30], car[30], c_add);
ppc ppc_0(c_add, cin, carry);
Fulladder adder_0(sum[30], car[30], carry, s);

initial
$monitor($time,"%dx%d=%d\n",e,f,s);
endmodule



