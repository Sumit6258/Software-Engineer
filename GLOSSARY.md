# Glossary

Short definitions of the terms introduced so far, each linking to the lesson that explains it properly. The glossary grows with the library; terms from lessons that have not been written yet are not defined here.

## A

- **Absorption**: In floating-point addition, the loss of a small operand when it is added to a much larger one, because the sum rounds back to the larger value. See [Floating-Point Representation and IEEE 754](docs/01-computer-science-foundations/01-computer-fundamentals/02-number-systems/05-floating-point-and-ieee-754.md).
- **ALU (arithmetic logic unit)**: The part of a processor that performs integer arithmetic and bitwise operations. See [Binary Arithmetic](docs/01-computer-science-foundations/01-computer-fundamentals/02-number-systems/03-binary-arithmetic.md).

## B

- **Bandwidth**: The amount of data a link can carry per unit of time. Not the same as latency. See [Client-Server and Remote Computing](docs/01-computer-science-foundations/01-computer-fundamentals/01-introduction-to-computers/03-client-server-and-remote-computing.md).
- **Base (radix)**: The number of distinct digit symbols in a positional system, and the factor between adjacent place values. See [Positional Number Systems](docs/01-computer-science-foundations/01-computer-fundamentals/02-number-systems/01-positional-number-systems.md).
- **Bias (exponent bias)**: A constant added to a floating-point exponent so that it can be stored as an unsigned field: 127 for binary32 and 1023 for binary64. See [Floating-Point Representation and IEEE 754](docs/01-computer-science-foundations/01-computer-fundamentals/02-number-systems/05-floating-point-and-ieee-754.md).
- **Binary-coded decimal (BCD)**: A code that stores each decimal digit in its own 4 bits. See [Positional Number Systems](docs/01-computer-science-foundations/01-computer-fundamentals/02-number-systems/01-positional-number-systems.md).
- **Bit**: A binary digit, 0 or 1; the smallest unit of information in a digital computer. See [Positional Number Systems](docs/01-computer-science-foundations/01-computer-fundamentals/02-number-systems/01-positional-number-systems.md).
- **Bitwise operation**: An operation applied independently to every bit position of its operands: AND, OR, XOR, NOT and shifts. See [Binary Arithmetic](docs/01-computer-science-foundations/01-computer-fundamentals/02-number-systems/03-binary-arithmetic.md).

## C

- **Carry**: The value passed to the next column when a column's sum is too large for one digit. See [Binary Arithmetic](docs/01-computer-science-foundations/01-computer-fundamentals/02-number-systems/03-binary-arithmetic.md).
- **Carry-lookahead adder**: An adder that computes all carries in parallel from generate and propagate signals instead of waiting for them to ripple. See [Binary Arithmetic](docs/01-computer-science-foundations/01-computer-fundamentals/02-number-systems/03-binary-arithmetic.md).
- **Catastrophic cancellation**: The loss of most significant digits when two nearly equal floating-point numbers are subtracted. See [Floating-Point Representation and IEEE 754](docs/01-computer-science-foundations/01-computer-fundamentals/02-number-systems/05-floating-point-and-ieee-754.md).
- **Client**: A program (or the machine running it) that initiates a request for a service. See [Client-Server and Remote Computing](docs/01-computer-science-foundations/01-computer-fundamentals/01-introduction-to-computers/03-client-server-and-remote-computing.md).
- **Computer**: A programmable machine that follows stored instructions to turn input into output, using memory to hold both instructions and data. See [What Is a Computer?](docs/01-computer-science-foundations/01-computer-fundamentals/01-introduction-to-computers/01-what-is-a-computer.md).

## E

- **Embedded computer**: A computer built into a larger product to control it, usually with a dedicated purpose. See [Types of Computers](docs/01-computer-science-foundations/01-computer-fundamentals/01-introduction-to-computers/02-types-of-computers.md).
- **Exascale**: Computing at $10^{18}$ floating-point operations per second. See [Types of Computers](docs/01-computer-science-foundations/01-computer-fundamentals/01-introduction-to-computers/02-types-of-computers.md).
- **Exponent (floating point)**: The field that scales the significand by a power of two. See [Floating-Point Representation and IEEE 754](docs/01-computer-science-foundations/01-computer-fundamentals/02-number-systems/05-floating-point-and-ieee-754.md).

## F

- **Firmware**: Software stored permanently in a device's own non-volatile memory and closely tied to that device. See [What Is a Computer?](docs/01-computer-science-foundations/01-computer-fundamentals/01-introduction-to-computers/01-what-is-a-computer.md).
- **Fixed-point**: A representation that stores a number as an integer with an agreed, fixed position of the radix point. See [Floating-Point Representation and IEEE 754](docs/01-computer-science-foundations/01-computer-fundamentals/02-number-systems/05-floating-point-and-ieee-754.md).
- **Floating-point**: A representation of numbers as a sign, an exponent and a fraction, like scientific notation in base 2. See [Floating-Point Representation and IEEE 754](docs/01-computer-science-foundations/01-computer-fundamentals/02-number-systems/05-floating-point-and-ieee-754.md).
- **Fraction (significand field)**: The field that holds the digits after the leading 1 of a floating-point number's significand. See [Floating-Point Representation and IEEE 754](docs/01-computer-science-foundations/01-computer-fundamentals/02-number-systems/05-floating-point-and-ieee-754.md).
- **Full adder and half adder**: Circuits that add bits: a half adder adds two bits; a full adder also accepts an incoming carry. See [Binary Arithmetic](docs/01-computer-science-foundations/01-computer-fundamentals/02-number-systems/03-binary-arithmetic.md).

## G

- **Gray code**: A binary code in which consecutive values differ in exactly one bit. See [Positional Number Systems](docs/01-computer-science-foundations/01-computer-fundamentals/02-number-systems/01-positional-number-systems.md).

## H

- **Hardware**: The physical equipment of a computer: processor, memory, storage, boards and devices. See [What Is a Computer?](docs/01-computer-science-foundations/01-computer-fundamentals/01-introduction-to-computers/01-what-is-a-computer.md).
- **Harvard architecture**: A design with separate memories for instructions and for data. See [What Is a Computer?](docs/01-computer-science-foundations/01-computer-fundamentals/01-introduction-to-computers/01-what-is-a-computer.md).
- **Hexadecimal**: Base 16, written with the digits 0 to 9 and A to F; each digit stands for exactly 4 bits. See [Positional Number Systems](docs/01-computer-science-foundations/01-computer-fundamentals/02-number-systems/01-positional-number-systems.md).
- **Hidden bit**: The leading 1 of a normal floating-point significand, which is implied and not stored. See [Floating-Point Representation and IEEE 754](docs/01-computer-science-foundations/01-computer-fundamentals/02-number-systems/05-floating-point-and-ieee-754.md).

## I

- **IEEE 754**: The standard that defines floating-point formats, rounding and special values. See [Floating-Point Representation and IEEE 754](docs/01-computer-science-foundations/01-computer-fundamentals/02-number-systems/05-floating-point-and-ieee-754.md).

## L

- **Latency**: The time a message takes to travel from one place to another. See [Client-Server and Remote Computing](docs/01-computer-science-foundations/01-computer-fundamentals/01-introduction-to-computers/03-client-server-and-remote-computing.md).
- **Loopback address**: An address that refers to the local machine itself; `127.0.0.1` in IPv4. See [Client-Server and Remote Computing](docs/01-computer-science-foundations/01-computer-fundamentals/01-introduction-to-computers/03-client-server-and-remote-computing.md).

## M

- **Machine epsilon**: The gap between 1.0 and the next larger representable floating-point number. See [Floating-Point Representation and IEEE 754](docs/01-computer-science-foundations/01-computer-fundamentals/02-number-systems/05-floating-point-and-ieee-754.md).
- **Memory (RAM)**: Fast, volatile working storage that the processor accesses directly by address. See [What Is a Computer?](docs/01-computer-science-foundations/01-computer-fundamentals/01-introduction-to-computers/01-what-is-a-computer.md).
- **Microcontroller**: A single-chip computer combining a small processor, memory and peripherals, used in embedded systems. See [Types of Computers](docs/01-computer-science-foundations/01-computer-fundamentals/01-introduction-to-computers/02-types-of-computers.md).

## N

- **NaN (not a number)**: The floating-point value produced by invalid operations; every comparison with it is false. See [Floating-Point Representation and IEEE 754](docs/01-computer-science-foundations/01-computer-fundamentals/02-number-systems/05-floating-point-and-ieee-754.md).
- **Nibble**: Four bits; one hexadecimal digit. See [Positional Number Systems](docs/01-computer-science-foundations/01-computer-fundamentals/02-number-systems/01-positional-number-systems.md).
- **Number and numeral**: A number is an abstract quantity; a numeral is a written representation of it, such as `13`, `XIII` or `1101`. See [Positional Number Systems](docs/01-computer-science-foundations/01-computer-fundamentals/02-number-systems/01-positional-number-systems.md).

## O

- **Octal**: Base 8; each digit stands for exactly 3 bits. See [Positional Number Systems](docs/01-computer-science-foundations/01-computer-fundamentals/02-number-systems/01-positional-number-systems.md).
- **Offset binary (excess-K)**: A representation that stores value plus a constant K as an unsigned number. See [Signed Numbers and Two's Complement](docs/01-computer-science-foundations/01-computer-fundamentals/02-number-systems/04-signed-numbers-and-twos-complement.md).
- **Ones' complement**: A signed representation in which a number is negated by inverting every bit. It has two zeros. See [Signed Numbers and Two's Complement](docs/01-computer-science-foundations/01-computer-fundamentals/02-number-systems/04-signed-numbers-and-twos-complement.md).
- **Overflow**: A result outside the representable range. For unsigned numbers it shows as a carry out of the top bit; for signed numbers it is detected by the sign rule. See [Signed Numbers and Two's Complement](docs/01-computer-science-foundations/01-computer-fundamentals/02-number-systems/04-signed-numbers-and-twos-complement.md).

## P

- **Positional notation**: A way of writing numbers in which a digit's position determines its weight. See [Positional Number Systems](docs/01-computer-science-foundations/01-computer-fundamentals/02-number-systems/01-positional-number-systems.md).
- **Protocol**: An agreed set of message formats and rules that lets a client and a server cooperate. See [Client-Server and Remote Computing](docs/01-computer-science-foundations/01-computer-fundamentals/01-introduction-to-computers/03-client-server-and-remote-computing.md).

## R

- **Round to nearest, ties to even**: The default IEEE 754 rounding rule: pick the nearest representable value, and on a tie the one with an even last bit. See [Floating-Point Representation and IEEE 754](docs/01-computer-science-foundations/01-computer-fundamentals/02-number-systems/05-floating-point-and-ieee-754.md).

## S

- **Saturation**: Clamping a result to the largest (or smallest) representable value instead of wrapping around. See [Binary Arithmetic](docs/01-computer-science-foundations/01-computer-fundamentals/02-number-systems/03-binary-arithmetic.md).
- **Server**: A program (or the machine running it) that waits for requests and provides a service. See [Client-Server and Remote Computing](docs/01-computer-science-foundations/01-computer-fundamentals/01-introduction-to-computers/03-client-server-and-remote-computing.md).
- **Sign extension**: Widening a signed value by copying its sign bit into the new high bits. See [Signed Numbers and Two's Complement](docs/01-computer-science-foundations/01-computer-fundamentals/02-number-systems/04-signed-numbers-and-twos-complement.md).
- **Sign-magnitude**: A signed representation with a sign bit and a magnitude. It has two zeros. See [Signed Numbers and Two's Complement](docs/01-computer-science-foundations/01-computer-fundamentals/02-number-systems/04-signed-numbers-and-twos-complement.md).
- **Stateless**: Describes a protocol in which each request carries everything needed to process it, so the server keeps no memory of earlier requests. See [Client-Server and Remote Computing](docs/01-computer-science-foundations/01-computer-fundamentals/01-introduction-to-computers/03-client-server-and-remote-computing.md).
- **Stored-program concept**: The design in which instructions and data are both held as bit patterns in the same memory. See [What Is a Computer?](docs/01-computer-science-foundations/01-computer-fundamentals/01-introduction-to-computers/01-what-is-a-computer.md).
- **Subnormal**: A floating-point number smaller than the smallest normal number, stored without a hidden bit, giving gradual underflow. See [Floating-Point Representation and IEEE 754](docs/01-computer-science-foundations/01-computer-fundamentals/02-number-systems/05-floating-point-and-ieee-754.md).
- **Supercomputer**: A system built to run one very large job across a very large number of processors in parallel. See [Types of Computers](docs/01-computer-science-foundations/01-computer-fundamentals/01-introduction-to-computers/02-types-of-computers.md).

## T

- **Two's complement**: The standard signed integer representation, in which the top bit has negative weight and negation is invert-and-add-one. See [Signed Numbers and Two's Complement](docs/01-computer-science-foundations/01-computer-fundamentals/02-number-systems/04-signed-numbers-and-twos-complement.md).

## U

- **Ulp (unit in the last place)**: The gap between a floating-point number and the next representable one. See [Floating-Point Representation and IEEE 754](docs/01-computer-science-foundations/01-computer-fundamentals/02-number-systems/05-floating-point-and-ieee-754.md).
- **Unsigned**: Interpreting a bit pattern as a non-negative integer from 0 to $2^n - 1$. See [Signed Numbers and Two's Complement](docs/01-computer-science-foundations/01-computer-fundamentals/02-number-systems/04-signed-numbers-and-twos-complement.md).

## V

- **Von Neumann architecture**: A stored-program design in which instructions and data share one memory. See [What Is a Computer?](docs/01-computer-science-foundations/01-computer-fundamentals/01-introduction-to-computers/01-what-is-a-computer.md).

## W

- **Wraparound**: Keeping only the low $n$ bits of a result, so values wrap modulo $2^n$. See [Binary Arithmetic](docs/01-computer-science-foundations/01-computer-fundamentals/02-number-systems/03-binary-arithmetic.md).
