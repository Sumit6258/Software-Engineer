# Glossary

Short definitions of the terms introduced so far, each linking to the lesson that explains it properly. The glossary grows with the library; terms from lessons that have not been written yet are not defined here.

## A

- **Absorption**: In floating-point addition, the loss of a small operand when it is added to a much larger one, because the sum rounds back to the larger value. See [Floating-Point Representation and IEEE 754](docs/01-computer-science-foundations/01-computer-fundamentals/02-number-systems/05-floating-point-and-ieee-754.md).
- **Address (memory address)**: The number that identifies one byte-sized cell of memory. See [Bits, Bytes, Words and Memory Addresses](docs/01-computer-science-foundations/01-computer-fundamentals/03-data-representation/01-bits-bytes-words-and-addresses.md).
- **Aliasing (sampling)**: The effect of sampling a signal too slowly, so that high frequencies appear as lower ones. See [Image, Audio and Video Encoding](docs/01-computer-science-foundations/01-computer-fundamentals/03-data-representation/06-image-audio-and-video-encoding.md).
- **Alignment**: Placing a value at an address that is a multiple of its size, which many processors require or prefer. See [Bits, Bytes, Words and Memory Addresses](docs/01-computer-science-foundations/01-computer-fundamentals/03-data-representation/01-bits-bytes-words-and-addresses.md).
- **ALU (arithmetic logic unit)**: The part of a processor that performs integer arithmetic and bitwise operations. See [Binary Arithmetic](docs/01-computer-science-foundations/01-computer-fundamentals/02-number-systems/03-binary-arithmetic.md).

## B

- **Backward and forward compatibility**: Backward: new code can read old data. Forward: old code can read new data, typically by ignoring unknown fields. See [Data Serialization](docs/01-computer-science-foundations/01-computer-fundamentals/03-data-representation/07-data-serialization.md).
- **Bandwidth**: The amount of data a link can carry per unit of time. Not the same as latency. See [Client-Server and Remote Computing](docs/01-computer-science-foundations/01-computer-fundamentals/01-introduction-to-computers/03-client-server-and-remote-computing.md).
- **Base (radix)**: The number of distinct digit symbols in a positional system, and the factor between adjacent place values. See [Positional Number Systems](docs/01-computer-science-foundations/01-computer-fundamentals/02-number-systems/01-positional-number-systems.md).
- **Bias (exponent bias)**: A constant added to a floating-point exponent so that it can be stored as an unsigned field: 127 for binary32 and 1023 for binary64. See [Floating-Point Representation and IEEE 754](docs/01-computer-science-foundations/01-computer-fundamentals/02-number-systems/05-floating-point-and-ieee-754.md).
- **Big-endian**: Byte order that stores the most significant byte at the lowest address. See [Integers, Floating-Point Numbers and Endianness in Memory](docs/01-computer-science-foundations/01-computer-fundamentals/03-data-representation/05-integers-floats-and-endianness-in-memory.md).
- **Binary-coded decimal (BCD)**: A code that stores each decimal digit in its own 4 bits. See [Positional Number Systems](docs/01-computer-science-foundations/01-computer-fundamentals/02-number-systems/01-positional-number-systems.md).
- **Bit**: A binary digit, 0 or 1; the smallest unit of information in a digital computer. See [Positional Number Systems](docs/01-computer-science-foundations/01-computer-fundamentals/02-number-systems/01-positional-number-systems.md).
- **Bit depth**: The number of bits used to store each sample or colour channel. See [Image, Audio and Video Encoding](docs/01-computer-science-foundations/01-computer-fundamentals/03-data-representation/06-image-audio-and-video-encoding.md).
- **Bitwise operation**: An operation applied independently to every bit position of its operands: AND, OR, XOR, NOT and shifts. See [Binary Arithmetic](docs/01-computer-science-foundations/01-computer-fundamentals/02-number-systems/03-binary-arithmetic.md).
- **Boolean algebra**: The algebra of two-valued quantities, with AND, OR and NOT and laws for transforming expressions. See [Boolean Algebra and De Morgan's Laws](docs/01-computer-science-foundations/01-computer-fundamentals/04-boolean-logic/02-boolean-algebra-and-de-morgans-laws.md).
- **Byte**: Eight bits in practice; the smallest addressable unit of memory. See [Bits, Bytes, Words and Memory Addresses](docs/01-computer-science-foundations/01-computer-fundamentals/03-data-representation/01-bits-bytes-words-and-addresses.md).
- **Byte order mark (BOM)**: The character U+FEFF placed at the start of text so a reader can tell the byte order or encoding. See [Unicode, UTF-8 and UTF-16](docs/01-computer-science-foundations/01-computer-fundamentals/03-data-representation/04-unicode-utf-8-and-utf-16.md).

## C

- **Carry**: The value passed to the next column when a column's sum is too large for one digit. See [Binary Arithmetic](docs/01-computer-science-foundations/01-computer-fundamentals/02-number-systems/03-binary-arithmetic.md).
- **Carry-lookahead adder**: An adder that computes all carries in parallel from generate and propagate signals instead of waiting for them to ripple. See [Binary Arithmetic](docs/01-computer-science-foundations/01-computer-fundamentals/02-number-systems/03-binary-arithmetic.md).
- **Catastrophic cancellation**: The loss of most significant digits when two nearly equal floating-point numbers are subtracted. See [Floating-Point Representation and IEEE 754](docs/01-computer-science-foundations/01-computer-fundamentals/02-number-systems/05-floating-point-and-ieee-754.md).
- **Character encoding**: A rule for writing the numbers of a character set as bytes. See [Character Encoding and ASCII](docs/01-computer-science-foundations/01-computer-fundamentals/03-data-representation/03-character-encoding-and-ascii.md).
- **Checksum**: A short value computed from data, such as a sum, used to detect accidental changes. See [Error Detection and Correction](docs/01-computer-science-foundations/01-computer-fundamentals/03-data-representation/02-error-detection-and-correction.md).
- **Chroma subsampling**: Storing colour at lower resolution than brightness, because the eye is less sensitive to colour detail. See [Image, Audio and Video Encoding](docs/01-computer-science-foundations/01-computer-fundamentals/03-data-representation/06-image-audio-and-video-encoding.md).
- **Client**: A program (or the machine running it) that initiates a request for a service. See [Client-Server and Remote Computing](docs/01-computer-science-foundations/01-computer-fundamentals/01-introduction-to-computers/03-client-server-and-remote-computing.md).
- **Code point**: The number Unicode assigns to a character, written U+ followed by hexadecimal digits. See [Unicode, UTF-8 and UTF-16](docs/01-computer-science-foundations/01-computer-fundamentals/03-data-representation/04-unicode-utf-8-and-utf-16.md).
- **Code unit**: The fixed-size piece an encoding is built from: one byte in UTF-8, 16 bits in UTF-16. See [Unicode, UTF-8 and UTF-16](docs/01-computer-science-foundations/01-computer-fundamentals/03-data-representation/04-unicode-utf-8-and-utf-16.md).
- **Codec and container**: A codec compresses and decompresses a stream; a container packages compressed streams into a file. See [Image, Audio and Video Encoding](docs/01-computer-science-foundations/01-computer-fundamentals/03-data-representation/06-image-audio-and-video-encoding.md).
- **Combinational logic**: Logic whose output depends only on its present inputs, with no memory. See [Logic Gates and Truth Tables](docs/01-computer-science-foundations/01-computer-fundamentals/04-boolean-logic/01-logic-gates-and-truth-tables.md).
- **Computer**: A programmable machine that follows stored instructions to turn input into output, using memory to hold both instructions and data. See [What Is a Computer?](docs/01-computer-science-foundations/01-computer-fundamentals/01-introduction-to-computers/01-what-is-a-computer.md).
- **CRC (cyclic redundancy check)**: An error-detecting code from polynomial division over GF(2), strong against bursts of errors. See [Error Detection and Correction](docs/01-computer-science-foundations/01-computer-fundamentals/03-data-representation/02-error-detection-and-correction.md).

## D

- **Data model (ILP32, LP64, LLP64)**: The set of sizes a C platform gives to int, long and pointers. See [Integers, Floating-Point Numbers and Endianness in Memory](docs/01-computer-science-foundations/01-computer-fundamentals/03-data-representation/05-integers-floats-and-endianness-in-memory.md).
- **De Morgan's laws**: The complement of an AND is the OR of the complements, and the complement of an OR is the AND of the complements. See [Boolean Algebra and De Morgan's Laws](docs/01-computer-science-foundations/01-computer-fundamentals/04-boolean-logic/02-boolean-algebra-and-de-morgans-laws.md).
- **Deserialization**: Rebuilding in-memory data from its serialized bytes. See [Data Serialization](docs/01-computer-science-foundations/01-computer-fundamentals/03-data-representation/07-data-serialization.md).
- **Don't-care condition**: An input combination whose output does not matter, which minimisation may treat as 0 or 1. See [Logic Simplification](docs/01-computer-science-foundations/01-computer-fundamentals/04-boolean-logic/03-logic-simplification.md).

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
- **Functional completeness (universal gate)**: A set of gates from which every Boolean function can be built; NAND alone and NOR alone are complete. See [Logic Gates and Truth Tables](docs/01-computer-science-foundations/01-computer-fundamentals/04-boolean-logic/01-logic-gates-and-truth-tables.md).

## G

- **Grapheme cluster**: What a reader perceives as one character, which may be several code points. See [Unicode, UTF-8 and UTF-16](docs/01-computer-science-foundations/01-computer-fundamentals/03-data-representation/04-unicode-utf-8-and-utf-16.md).
- **Gray code**: A binary code in which consecutive values differ in exactly one bit. See [Positional Number Systems](docs/01-computer-science-foundations/01-computer-fundamentals/02-number-systems/01-positional-number-systems.md).

## H

- **Hamming code**: A family of codes that adds parity bits so that a single flipped bit can be located and corrected. See [Error Detection and Correction](docs/01-computer-science-foundations/01-computer-fundamentals/03-data-representation/02-error-detection-and-correction.md).
- **Hamming distance**: The number of positions in which two equal-length bit strings differ. See [Error Detection and Correction](docs/01-computer-science-foundations/01-computer-fundamentals/03-data-representation/02-error-detection-and-correction.md).
- **Hardware**: The physical equipment of a computer: processor, memory, storage, boards and devices. See [What Is a Computer?](docs/01-computer-science-foundations/01-computer-fundamentals/01-introduction-to-computers/01-what-is-a-computer.md).
- **Harvard architecture**: A design with separate memories for instructions and for data. See [What Is a Computer?](docs/01-computer-science-foundations/01-computer-fundamentals/01-introduction-to-computers/01-what-is-a-computer.md).
- **Hexadecimal**: Base 16, written with the digits 0 to 9 and A to F; each digit stands for exactly 4 bits. See [Positional Number Systems](docs/01-computer-science-foundations/01-computer-fundamentals/02-number-systems/01-positional-number-systems.md).
- **Hidden bit**: The leading 1 of a normal floating-point significand, which is implied and not stored. See [Floating-Point Representation and IEEE 754](docs/01-computer-science-foundations/01-computer-fundamentals/02-number-systems/05-floating-point-and-ieee-754.md).

## I

- **IEEE 754**: The standard that defines floating-point formats, rounding and special values. See [Floating-Point Representation and IEEE 754](docs/01-computer-science-foundations/01-computer-fundamentals/02-number-systems/05-floating-point-and-ieee-754.md).

## K

- **Karnaugh map**: A truth table arranged on a grid with Gray-code axes so that groups of adjacent 1s give simplified product terms. See [Logic Simplification](docs/01-computer-science-foundations/01-computer-fundamentals/04-boolean-logic/03-logic-simplification.md).
- **Kibibyte (KiB), mebibyte, gibibyte**: Binary size units of 2 to the power 10, 20 and 30 bytes; kB, MB and GB mean powers of 1000. See [Bits, Bytes, Words and Memory Addresses](docs/01-computer-science-foundations/01-computer-fundamentals/03-data-representation/01-bits-bytes-words-and-addresses.md).

## L

- **Latency**: The time a message takes to travel from one place to another. See [Client-Server and Remote Computing](docs/01-computer-science-foundations/01-computer-fundamentals/01-introduction-to-computers/03-client-server-and-remote-computing.md).
- **Little-endian**: Byte order that stores the least significant byte at the lowest address. See [Integers, Floating-Point Numbers and Endianness in Memory](docs/01-computer-science-foundations/01-computer-fundamentals/03-data-representation/05-integers-floats-and-endianness-in-memory.md).
- **Logic gate**: A circuit that computes a Boolean function of one or more binary inputs. See [Logic Gates and Truth Tables](docs/01-computer-science-foundations/01-computer-fundamentals/04-boolean-logic/01-logic-gates-and-truth-tables.md).
- **Loopback address**: An address that refers to the local machine itself; `127.0.0.1` in IPv4. See [Client-Server and Remote Computing](docs/01-computer-science-foundations/01-computer-fundamentals/01-introduction-to-computers/03-client-server-and-remote-computing.md).
- **Lossless and lossy compression**: Lossless compression is exactly reversible; lossy compression discards information to be smaller. See [Image, Audio and Video Encoding](docs/01-computer-science-foundations/01-computer-fundamentals/03-data-representation/06-image-audio-and-video-encoding.md).

## M

- **Machine epsilon**: The gap between 1.0 and the next larger representable floating-point number. See [Floating-Point Representation and IEEE 754](docs/01-computer-science-foundations/01-computer-fundamentals/02-number-systems/05-floating-point-and-ieee-754.md).
- **Memory (RAM)**: Fast, volatile working storage that the processor accesses directly by address. See [What Is a Computer?](docs/01-computer-science-foundations/01-computer-fundamentals/01-introduction-to-computers/01-what-is-a-computer.md).
- **Microcontroller**: A single-chip computer combining a small processor, memory and peripherals, used in embedded systems. See [Types of Computers](docs/01-computer-science-foundations/01-computer-fundamentals/01-introduction-to-computers/02-types-of-computers.md).
- **Minterm and maxterm**: A minterm is a product that is 1 for exactly one input row; a maxterm is a sum that is 0 for exactly one row. See [Boolean Algebra and De Morgan's Laws](docs/01-computer-science-foundations/01-computer-fundamentals/04-boolean-logic/02-boolean-algebra-and-de-morgans-laws.md).
- **Mojibake**: Garbled text that results from decoding bytes with a different encoding from the one used to write them. See [Character Encoding and ASCII](docs/01-computer-science-foundations/01-computer-fundamentals/03-data-representation/03-character-encoding-and-ascii.md).

## N

- **NaN (not a number)**: The floating-point value produced by invalid operations; every comparison with it is false. See [Floating-Point Representation and IEEE 754](docs/01-computer-science-foundations/01-computer-fundamentals/02-number-systems/05-floating-point-and-ieee-754.md).
- **Network byte order**: Big-endian order, specified for multi-byte fields in Internet protocols. See [Integers, Floating-Point Numbers and Endianness in Memory](docs/01-computer-science-foundations/01-computer-fundamentals/03-data-representation/05-integers-floats-and-endianness-in-memory.md).
- **Nibble**: Four bits; one hexadecimal digit. See [Positional Number Systems](docs/01-computer-science-foundations/01-computer-fundamentals/02-number-systems/01-positional-number-systems.md).
- **Normalisation (Unicode)**: Converting equivalent code-point sequences to one canonical form, such as NFC. See [Unicode, UTF-8 and UTF-16](docs/01-computer-science-foundations/01-computer-fundamentals/03-data-representation/04-unicode-utf-8-and-utf-16.md).
- **Number and numeral**: A number is an abstract quantity; a numeral is a written representation of it, such as `13`, `XIII` or `1101`. See [Positional Number Systems](docs/01-computer-science-foundations/01-computer-fundamentals/02-number-systems/01-positional-number-systems.md).
- **Nyquist-Shannon sampling theorem**: A signal limited to frequencies below f can be reconstructed from samples taken at more than 2f. See [Image, Audio and Video Encoding](docs/01-computer-science-foundations/01-computer-fundamentals/03-data-representation/06-image-audio-and-video-encoding.md).

## O

- **Octal**: Base 8; each digit stands for exactly 3 bits. See [Positional Number Systems](docs/01-computer-science-foundations/01-computer-fundamentals/02-number-systems/01-positional-number-systems.md).
- **Octet**: Exactly 8 bits; the term Internet standards use for a byte. See [Bits, Bytes, Words and Memory Addresses](docs/01-computer-science-foundations/01-computer-fundamentals/03-data-representation/01-bits-bytes-words-and-addresses.md).
- **Offset binary (excess-K)**: A representation that stores value plus a constant K as an unsigned number. See [Signed Numbers and Two's Complement](docs/01-computer-science-foundations/01-computer-fundamentals/02-number-systems/04-signed-numbers-and-twos-complement.md).
- **Ones' complement**: A signed representation in which a number is negated by inverting every bit. It has two zeros. See [Signed Numbers and Two's Complement](docs/01-computer-science-foundations/01-computer-fundamentals/02-number-systems/04-signed-numbers-and-twos-complement.md).
- **Overflow**: A result outside the representable range. For unsigned numbers it shows as a carry out of the top bit; for signed numbers it is detected by the sign rule. See [Signed Numbers and Two's Complement](docs/01-computer-science-foundations/01-computer-fundamentals/02-number-systems/04-signed-numbers-and-twos-complement.md).

## P

- **Padding**: Unused bytes a compiler inserts so that fields are aligned. See [Bits, Bytes, Words and Memory Addresses](docs/01-computer-science-foundations/01-computer-fundamentals/03-data-representation/01-bits-bytes-words-and-addresses.md).
- **Parity bit**: An extra bit chosen to make the number of 1 bits even (or odd); detects any odd number of flipped bits. See [Error Detection and Correction](docs/01-computer-science-foundations/01-computer-fundamentals/03-data-representation/02-error-detection-and-correction.md).
- **Pixel**: One element of a raster image, usually stored as red, green and blue intensities. See [Image, Audio and Video Encoding](docs/01-computer-science-foundations/01-computer-fundamentals/03-data-representation/06-image-audio-and-video-encoding.md).
- **Pointer**: A variable whose value is a memory address. See [Bits, Bytes, Words and Memory Addresses](docs/01-computer-science-foundations/01-computer-fundamentals/03-data-representation/01-bits-bytes-words-and-addresses.md).
- **Positional notation**: A way of writing numbers in which a digit's position determines its weight. See [Positional Number Systems](docs/01-computer-science-foundations/01-computer-fundamentals/02-number-systems/01-positional-number-systems.md).
- **Prime implicant**: A product term that implies the function and cannot be shrunk by removing a variable. See [Logic Simplification](docs/01-computer-science-foundations/01-computer-fundamentals/04-boolean-logic/03-logic-simplification.md).
- **Protocol**: An agreed set of message formats and rules that lets a client and a server cooperate. See [Client-Server and Remote Computing](docs/01-computer-science-foundations/01-computer-fundamentals/01-introduction-to-computers/03-client-server-and-remote-computing.md).

## Q

- **Quine-McCluskey algorithm**: A systematic procedure that merges minterms into prime implicants and then selects a minimal cover. See [Logic Simplification](docs/01-computer-science-foundations/01-computer-fundamentals/04-boolean-logic/03-logic-simplification.md).

## R

- **Redundancy**: Extra information added to data so that damage can be detected or repaired. See [Error Detection and Correction](docs/01-computer-science-foundations/01-computer-fundamentals/03-data-representation/02-error-detection-and-correction.md).
- **Round to nearest, ties to even**: The default IEEE 754 rounding rule: pick the nearest representable value, and on a tie the one with an even last bit. See [Floating-Point Representation and IEEE 754](docs/01-computer-science-foundations/01-computer-fundamentals/02-number-systems/05-floating-point-and-ieee-754.md).

## S

- **Sample rate**: The number of measurements of a signal taken per second. See [Image, Audio and Video Encoding](docs/01-computer-science-foundations/01-computer-fundamentals/03-data-representation/06-image-audio-and-video-encoding.md).
- **Saturation**: Clamping a result to the largest (or smallest) representable value instead of wrapping around. See [Binary Arithmetic](docs/01-computer-science-foundations/01-computer-fundamentals/02-number-systems/03-binary-arithmetic.md).
- **Schema**: A declared description of the structure of data. See [Data Serialization](docs/01-computer-science-foundations/01-computer-fundamentals/03-data-representation/07-data-serialization.md).
- **SECDED**: Single-error-correcting, double-error-detecting code, as used in ECC memory. See [Error Detection and Correction](docs/01-computer-science-foundations/01-computer-fundamentals/03-data-representation/02-error-detection-and-correction.md).
- **Serialization**: Converting in-memory data into a sequence of bytes for storage or transmission. See [Data Serialization](docs/01-computer-science-foundations/01-computer-fundamentals/03-data-representation/07-data-serialization.md).
- **Server**: A program (or the machine running it) that waits for requests and provides a service. See [Client-Server and Remote Computing](docs/01-computer-science-foundations/01-computer-fundamentals/01-introduction-to-computers/03-client-server-and-remote-computing.md).
- **Sign extension**: Widening a signed value by copying its sign bit into the new high bits. See [Signed Numbers and Two's Complement](docs/01-computer-science-foundations/01-computer-fundamentals/02-number-systems/04-signed-numbers-and-twos-complement.md).
- **Sign-magnitude**: A signed representation with a sign bit and a magnitude. It has two zeros. See [Signed Numbers and Two's Complement](docs/01-computer-science-foundations/01-computer-fundamentals/02-number-systems/04-signed-numbers-and-twos-complement.md).
- **Stateless**: Describes a protocol in which each request carries everything needed to process it, so the server keeps no memory of earlier requests. See [Client-Server and Remote Computing](docs/01-computer-science-foundations/01-computer-fundamentals/01-introduction-to-computers/03-client-server-and-remote-computing.md).
- **Stored-program concept**: The design in which instructions and data are both held as bit patterns in the same memory. See [What Is a Computer?](docs/01-computer-science-foundations/01-computer-fundamentals/01-introduction-to-computers/01-what-is-a-computer.md).
- **Subnormal**: A floating-point number smaller than the smallest normal number, stored without a hidden bit, giving gradual underflow. See [Floating-Point Representation and IEEE 754](docs/01-computer-science-foundations/01-computer-fundamentals/02-number-systems/05-floating-point-and-ieee-754.md).
- **Sum of products and product of sums**: Two standard forms of a Boolean expression: an OR of AND terms, or an AND of OR terms. See [Boolean Algebra and De Morgan's Laws](docs/01-computer-science-foundations/01-computer-fundamentals/04-boolean-logic/02-boolean-algebra-and-de-morgans-laws.md).
- **Supercomputer**: A system built to run one very large job across a very large number of processors in parallel. See [Types of Computers](docs/01-computer-science-foundations/01-computer-fundamentals/01-introduction-to-computers/02-types-of-computers.md).
- **Surrogate pair**: Two UTF-16 code units that together encode a code point above U+FFFF. See [Unicode, UTF-8 and UTF-16](docs/01-computer-science-foundations/01-computer-fundamentals/03-data-representation/04-unicode-utf-8-and-utf-16.md).

## T

- **Tag-length-value (TLV)**: A format in which each field is a tag, a length and a value, so readers can skip unknown fields. See [Data Serialization](docs/01-computer-science-foundations/01-computer-fundamentals/03-data-representation/07-data-serialization.md).
- **Truth table**: A table listing a function's output for every combination of inputs. See [Logic Gates and Truth Tables](docs/01-computer-science-foundations/01-computer-fundamentals/04-boolean-logic/01-logic-gates-and-truth-tables.md).
- **Two's complement**: The standard signed integer representation, in which the top bit has negative weight and negation is invert-and-add-one. See [Signed Numbers and Two's Complement](docs/01-computer-science-foundations/01-computer-fundamentals/02-number-systems/04-signed-numbers-and-twos-complement.md).

## U

- **Ulp (unit in the last place)**: The gap between a floating-point number and the next representable one. See [Floating-Point Representation and IEEE 754](docs/01-computer-science-foundations/01-computer-fundamentals/02-number-systems/05-floating-point-and-ieee-754.md).
- **Unicode**: The standard that assigns a unique code point to every character of every writing system. See [Unicode, UTF-8 and UTF-16](docs/01-computer-science-foundations/01-computer-fundamentals/03-data-representation/04-unicode-utf-8-and-utf-16.md).
- **Unsigned**: Interpreting a bit pattern as a non-negative integer from 0 to $2^n - 1$. See [Signed Numbers and Two's Complement](docs/01-computer-science-foundations/01-computer-fundamentals/02-number-systems/04-signed-numbers-and-twos-complement.md).
- **UTF-16**: A Unicode encoding that uses one or two 16-bit code units per code point. See [Unicode, UTF-8 and UTF-16](docs/01-computer-science-foundations/01-computer-fundamentals/03-data-representation/04-unicode-utf-8-and-utf-16.md).
- **UTF-8**: A variable-length Unicode encoding of one to four bytes that is ASCII-compatible. See [Unicode, UTF-8 and UTF-16](docs/01-computer-science-foundations/01-computer-fundamentals/03-data-representation/04-unicode-utf-8-and-utf-16.md).

## V

- **Von Neumann architecture**: A stored-program design in which instructions and data share one memory. See [What Is a Computer?](docs/01-computer-science-foundations/01-computer-fundamentals/01-introduction-to-computers/01-what-is-a-computer.md).

## W

- **Word**: The natural unit of data of a processor, commonly 16, 32 or 64 bits. See [Bits, Bytes, Words and Memory Addresses](docs/01-computer-science-foundations/01-computer-fundamentals/03-data-representation/01-bits-bytes-words-and-addresses.md).
- **Wraparound**: Keeping only the low $n$ bits of a result, so values wrap modulo $2^n$. See [Binary Arithmetic](docs/01-computer-science-foundations/01-computer-fundamentals/02-number-systems/03-binary-arithmetic.md).

## X

- **XOR (exclusive or)**: A gate that outputs 1 when exactly one input is 1; addition of two bits without carry. See [Logic Gates and Truth Tables](docs/01-computer-science-foundations/01-computer-fundamentals/04-boolean-logic/01-logic-gates-and-truth-tables.md).
