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
        
        S = random.randint(0,31)
	    I = [] 
        I0 = random.randint(0,4)

        #input driving

        dut.sel.value = S

        await Timer(2, units='ns')

        dut._log.info(f'S={S:05} I0={I0:05} model={I[S]:05} DUT={int(dut.out.value):05}')
        assert dut.out.value == I[S], "Randomised test failed with: {I[S]} = [OUT]".format(I[S]=dut.inp[S].value, OUT=dut.out.value)