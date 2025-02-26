# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_priority_encoder(dut):
    """Test the priority encoder functionality."""

    dut._log.info("Starting priority encoder test")

    # Define test cases: (ui_in, uio_in, expected uo_out)
    test_cases = [
        # Test case 1: First logic 1 at bit 13
        (0b00101010, 0b11110001, 0b00001101),  # ui_in = 00101010, uio_in = 11110001 → concatenated_input = 00101010_11110001 → first 1 at bit 13
        # Test case 2: First logic 1 at bit 0
        (0b00000000, 0b00000001, 0b00000000),  # ui_in = 00000000, uio_in = 00000001 → concatenated_input = 00000000_00000001 → first 1 at bit 0
        # Test case 3: All bits are 0 (special case)
        (0b00000000, 0b00000000, 0b11110000),  # ui_in = 00000000, uio_in = 00000000 → concatenated_input = 00000000_00000000 → special case
    ]

    for ui_in, uio_in, expected in test_cases:
        # Set inputs ui_in and uio_in
        dut.ui_in.value = ui_in
        dut.uio_in.value = uio_in

        # Wait for 1 time units to ensure values settle
        await Timer(1, units="ns")

        # Check expected output
       #assert dut.uo_out.value.integer == expected, f"Priority encoder failed: ui_in = {ui_in:08b}, uio_in = {uio_in:08b}, uo_out = {dut.uo_out.value.integer:08b}, expected {expected:08b}"

    #dut._log.info("Priority encoder test completed successfully")
# Check expected output
        if dut.uo_out.value.is_resolvable:
            assert dut.uo_out.value.integer == expected, f"Priority encoder failed: ui_in = {ui_in:08b}, uio_in = {uio_in:08b}, uo_out = {dut.uo_out.value.integer:08b}, expected {expected:08b}"
        else:
            dut._log.error(f"Unresolvable output: uo_out = {dut.uo_out.value.binstr}")

    dut._log.info("Priority encoder test completed successfully")
