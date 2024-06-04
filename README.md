SoldierCrab
-----------

<sup>WARN: :construction: under construction! :construction: - this hardware is under active development</sup>

[**SoldierCrab**](https://en.wikipedia.org/wiki/Mictyris_longicarpus) is an embeddable FPGA SoM (System-on-Module) designed for use in high-speed audio and USB applications.
It is the brain of [tiliqua](https://github.com/apfelaudio/tiliqua) and other [apfelaudio products](https://apfelaudio.com/).

**SoldierCrab** has the following core features:
- ECP5 FPGA (-25K or -45K variant in caBGA256 package)
- HyperRAM / oSPI-RAM (> 1Gb/sec bandwidth)
- USB2 PHY with exposed ID, it can be used in device or host mode
- 1V1 / 1V8 / 2V5 regulators onboard, 3V3 is all that's needed
- PROGRAMN internally exposed for multibooting bitstreams
- 2 indicator LEDs on the PCBA
- 48MHz master clock
- Card edge is basically: 45 exposed general purpose pins + 4-pin JTAG + USB2
- 22mmx22mm board size with M.2 E-key card edge (see 'Physical Compatibility' below)

Physical Compatibility
----------------------

**The SoldierCrab is 22mmx22mm with an M.2 E-key connector and offset mounting hole**. The mounting hole is offset such that this board is physically compatible with the SparkFun MicroMod format, however we **do not claim electrical compatibility with it** (even though this SoM will work with some MicroMod boards, the JTAG and I2C connections are in the wrong place for us to claim compatibility - this is intentional design choice to save routing space whilst trying to remain close to some kind of SoM standard).

## Builds on the following (awesome) open-hardware projects
- The [Cynthion](https://github.com/greatscottgadgets/cynthion-hardware) project from Great Scott Gadgets.
- The [OrangeCrab](https://github.com/orangecrab-fpga/orangecrab-hardware) project from Greg Davill.
- [Sparkfun Micromod](https://www.sparkfun.com/micromod).

# License

**Copyright (C) 2024 S. Holzapfel, apfelaudio UG (haftungsbeschränkt)**

The files in this project are largely covered under the CERN Open-Hardware License V2 CERN-OHL-S, mirrored in the LICENSE text in this repository. This LICENSE and copyright notice do NOT apply to imported artifacts in this repository (i.e datasheets, third-party 3D models, symbols or footprints), or to dependencies released under a different (but compatible) open-source license.
