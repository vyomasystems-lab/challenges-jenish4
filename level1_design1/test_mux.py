# See LICENSE.vyoma for details
# See LICENSE.cocotb for details

import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
    print("Test Started")
    cocotb.log.info('##### CTB: Develop your test here ########')

    for i in range (10):
        
        S = random.randint(0,30)
        I = []
        for j in range (31):
            I.append(random.randint(0,3))            	    
        
        #input driving

        dut.sel.value = S
        dut.inp0.value = I[0]
        dut.inp1.value = I[1]
        dut.inp2.value = I[2]
        dut.inp3.value = I[3]
        dut.inp4.value = I[4]
        dut.inp5.value = I[5]
        dut.inp6.value = I[6]
        dut.inp7.value = I[7]
        dut.inp8.value = I[8]
        dut.inp9.value = I[9]
        dut.inp10.value = I[10]
        dut.inp11.value = I[11]
        dut.inp12.value = I[12]
        dut.inp13.value = I[13]
        dut.inp14.value = I[14]
        dut.inp15.value = I[15]
        dut.inp16.value = I[16]
        dut.inp17.value = I[17]
        dut.inp18.value = I[18]
        dut.inp19.value = I[19]
        dut.inp20.value = I[20]
        dut.inp21.value = I[21]
        dut.inp22.value = I[22]
        dut.inp23.value = I[23]
        dut.inp24.value = I[24]
        dut.inp25.value = I[25]
        dut.inp26.value = I[26]
        dut.inp27.value = I[27]
        dut.inp28.value = I[28]
        dut.inp29.value = I[29]
        dut.inp30.value = I[30]

        await Timer(2, units='ns')

    #    dut._log.info(f'S={S:05} I0={I0:05} model={I[S]:05} DUT={int(dut.out.value):05}')
        assert dut.out.value == I[S], "Randomised test failed with: expected value={EXP}, output={OUTPUT}".format(EXP=I[S], OUTPUT=dut.out.value)
