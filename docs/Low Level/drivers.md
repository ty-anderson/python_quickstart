# Drivers

A driver is a special kind of program that acts as the "translator"
between the OS and a piece of hardware.

The hardware speaks its own low-level language (signals, registers, protocols).
The OS needs a way to understand that language in a consistent way.

Because it needs to interact with the OS, good drivers are written with
a language that compiles to machine code (C, Rust, Zig, etc.).

## When

The only time a developer would need to create a driver is if there is
new hardware. Maybe a brand new hardware your company made or that you
invented. This is because it requires deep knowledge of how the hardware 
works internally.

Creating drivers falls more into systems engineering/hardware engineering.

**Summary: Make hardware? You'll need to make drivers...**