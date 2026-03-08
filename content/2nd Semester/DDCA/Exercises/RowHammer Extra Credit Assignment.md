## Summary

The talk covers the discovery and ongoing story of RowHammer, a hardware vulnerability in DRAM by induced bit flips. 

As DRAM cells shrink and get closer together, they start interfering with each other electrically. By repeatedly activating the same memory row (hammering it), an attacker can flip bits in neighboring rows belonging to other programs or the OS, breaking memory isolation. Onur Mutlu's group found this while studying DRAM scaling and read disturbance, tested 129 modules from all three major manufacturers, and found over 80% vulnerable. 

Google Project Zero later turned it into a full Linux kernel exploit, which makes RowHammer a security (and confidentiality) issue instead of a simple reliability problem. Things have gotten worse over time with newer chips flip bits after as few as 4,800 row activations, and the newer RowPress attack can flip bits with fewer activations by keeping a row active. 

Proposed solutions include PARA, activating neighboring rows of a recently closed ones occasionally. Still, RowHammer remains unsolved and system-level solutions are needed.

## Strengths and Weaknesses

#### Strengths

1. The work is first to demonstrate how a simple physical hardware failure can bypass all software layers to create a widespread system security issue. This aligns with the statement from our first DDCA lecture, that Software is only ever as good as the Hardware it's on.
2. The talk nicely presents the path to the discovery and backgrounds as to how the group got to the given result. Also it shows an interesting pan from academia to a real-world issue (due to Google's Project Zero taking over the kernel). This also shows how serious the issue is and what the impact (and problem) of direct scaling is. 
3. Strong empirical evidence, as over 1,500 chips were tested across generations and producers in the rework years after the initial launch.
4. The program used were open sourced and allowed for collaboration with other institutions and companies. Very interessting to see how different companies reflect on the given issue. 

#### Weaknesses

1. Low coverage of OS-Level solutions. F.ex., how would it be possible to have the OS physical memory allocator isolate security critical elements away from regions that untrussted processes might hammer?
2. It was mentionned that all solutions are trade-offs between cost, power, performance, and complexity. But which solution comes in where in this scale is not mentionned. 

## Learnings and Thoughts

Watching the talk on RowHammer and researching surrounding topics made me learn a lot. I learned that memory isolation is this crucial for modern security, that it is physically fragile, and both a reliability and security issue. I also found it surprising that the industry largely tried to hide the problem rather than solve it, and that reverse engineering was needed just to understand what mitigations were even deployed.

Lastly, I was surprised how quickly the needed hammering reduced in recent years. So generally, how technology scaling introduces new failure modes that can't be ignored by system designers and that weren't visible in the beginning (this also applies to other areas, including in software such as LLM training), and, most importantly, how smart engineering that combines software and hardware can lead to more secure technology. 