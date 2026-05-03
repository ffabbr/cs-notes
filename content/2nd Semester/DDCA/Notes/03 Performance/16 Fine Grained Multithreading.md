
keep the pipeline busy by always having a ready instruction from some thread.

- CPU holds register state for multiple threads simultaneously
- latency of one thread is overlapped with work from others

single-thread performance worse (a thread only gets 1 out of N cycles), but overall throughput improves.
