# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_priority_16_8_encode(dut):
    """Test the priority encoder functionality with concatenation."""

    dut._log.info("Starting priority encoder test with concatenation")

    # Define test cases: (ui_in, uio_in, expected uo_out)
    test_cases = [
        # Test case 1: First logic 1 at bit 13
        (0b00101010, 0b11110001, 0b00001101),  # ui_in = 00101010, uio_in = 11110001 → concatenated_input = 00101010_11110001 → first 1 at bit 13
        # Test case 2: First logic 1 at bit 0
        (0b00000000, 0b00000001, 0b00000000),  # ui_in = 00000000, uio_in = 00000001 → concatenated_input = 00000000_00000001 → first 1 at bit 0
        # Test case 3: All bits are 0 (special case)
        (0b00000000, 0b00000000, 0b11110000),  # ui_in = 00000000, uio_in = 00000000 → concatenated_input = 00000000_00000000 → special case
        # Test case 4: First logic 1 at bit 7
        (0b00000000, 0b10000000, 0b00000111),  # ui_in = 00000000, uio_in = 10000000 → concatenated_input = 00000000_10000000 → first 1 at bit 7
        # Test case 5: First logic 1 at bit 15
        (0b10000000, 0b00000000, 0b00001111),  # ui_in = 10000000, uio_in = 00000000 → concatenated_input = 10000000_00000000 → first 1 at bit 15
    ]

    for ui_in, uio_in, expected in test_cases:
        # Set inputs ui_in and uio_in
        dut.ui_in.value = ui_in
        dut.uio_in.value = uio_in

        # Wait for 10 time units to ensure values settle
        await Timer(1, units="ns")

        # Check expected output
        assert dut.uo_out.value == expected, f"Priority encoder failed: ui_in = {ui_in:08b}, uio_in = {uio_in:08b}, uo_out = {dut.uo_out.value:08b}, expected {expected:08b}"

    dut._log.info("Priority encoder test with concatenation completed successfully")
