# process manager
??? note
	- program: the written code
	- process: a program that has started to be execute
	- PCB: data structure which contains all of the data needed for a process to run, created in memory when data is needed for execution. It stores:
		- process state
		- process privileges
		- scheduling information and priority
		- estimated execution time
		- pid
		- io status info: io allocated to process, list of open files
		- register values (PC, MAR,MDR,ACC)
	- process context: machine env while the process is running
		- program counter: location of instruction to next execute
		- CPU register: contents of all process-centric register
	- multitasking: computer can carry out more than one task at a time. Each of these processes share common io device. Works by scheduling routine.
	- multiprogramming: allows multiple programs to be loaded into memory and executed concurrently on a single processor
	- low level scheduler: cpu allocator
	- high level scheduler: memory allocator